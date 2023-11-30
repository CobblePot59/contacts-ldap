from flask import render_template, request, redirect, url_for, flash
from app import app, db, images
from models import Company, Employee, Tag
from decor import login_required
import os
import re
from sqlalchemy.exc import IntegrityError


@app.route('/', methods=['GET'])
@login_required
def companies():
    companies = Company.query.all()
    return render_template('companies.html', number = len(companies), companies = companies)

@app.route('/company/<company_name>', methods=['GET'])
@login_required
def get_company(company_name):
    companies = Company.query.all()
    company = Company.query.filter_by(name=company_name).first()
    return render_template('employees.html', title = f'Employees of {company_name}', number = len(company.employees), employee = company.employees, companies = companies)

@app.route('/add-company', methods=['POST'])
@login_required
def add_company():
    name = request.form['company-name']
    address = request.form['company-address']
    phone = request.form['company-phone']
    website = request.form['company-website']
    str_tags = request.form['company-tags']

    pattern = r'^0\d(\s?\d{2}){4}$'
    if not re.match(pattern, phone) and phone != '':
        flash('A valid phone number is required !', 'error')
        return redirect(url_for('companies'))

    pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+)\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?\/?$'
    if not re.match(pattern, website) and website != '':
        flash('A valid URL is required !', 'error')
        return redirect(url_for('companies'))

    try:
        company = Company(name = name, address = address, phone = phone, website = website)
        db.session.add(company)
        db.session.commit()
    except IntegrityError:
        flash('Company already registred', 'error')
        return redirect(url_for('companies'))

    q = Company.query.filter_by(name = name).first()
    for tag_name in str_tags.split(','):
        tag = Tag(name = tag_name.strip().lower(), company_id = q.id)
        db.session.add(tag)
        db.session.commit()

    flash('Company has been created', 'success')
    return redirect(url_for('companies'))

@app.route('/edit-company', methods=['POST'])
@login_required
def edit_company():
    _id = request.form['edit-company-id']
    name = request.form['edit-company-name']
    address = request.form['edit-company-address']
    phone = request.form['edit-company-phone']
    website = request.form['edit-company-website']
    str_tags = request.form['edit-company-tags']

    pattern = r'^0\d(\s?\d{2}){4}$'
    if not re.match(pattern, phone) and phone != '':
        flash('A valid phone number is required !', 'error')
        return redirect(url_for('companies'))

    pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+)\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?\/?$'
    if not re.match(pattern, website) and website != '':
        flash('A valid URL is required !', 'error')
        return redirect(url_for('companies'))

    company = Company.query.filter_by(id = _id).first()
    old_name = company.name

    company.name = name
    company.address = address
    company.phone = phone
    company.website = website

    employees = Employee.query.filter_by(company_name=old_name).all()
    for employee in employees:
        employee.company_name = name

    db.session.commit()

    company_tags = company.tags
    for tag in company_tags:
        Tag.query.filter_by(company_id = company.id).delete()

    for tag_name in str_tags.split(','):
        tag = Tag(name = tag_name.strip().lower(), company_id = company.id)
        db.session.add(tag)
        db.session.commit()
    flash('Company has been modified', 'success')
    return redirect(url_for('companies'))

@app.route('/remove-company', methods=['POST'])
@login_required
def remove_company():
    _id = request.form['rm-company-id']
    company = Company.query.filter_by(id = _id).first()

    Company.query.filter_by(id = _id).delete()

    company_tags = company.tags
    for tag in company_tags:
        Tag.query.filter_by(company_id = company.id).delete()
    db.session.commit()
    flash('Company has been removed', 'error')
    return redirect(url_for('companies'))

@app.route('/set-company-image', methods=['POST'])
@login_required
def company_image():
    _id = request.form['upload-company-id']
    company = Company.query.filter_by(id = _id).first()
    if "image" in request.files:
        image = request.files["image"]
        image_name = f'{company.name}.jpg'
        image_path = f'static/img/contacts/{image_name}'
        if os.path.exists(image_path):
            os.remove(image_path)
        images.save(image, name = image_name)
        company.image = image_name
        db.session.commit()
    return redirect(url_for('companies'))
