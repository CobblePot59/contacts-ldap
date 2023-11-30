from flask import render_template, request, redirect, url_for, flash
from app import app, db, images
from models import Company, Employee
from decor import login_required
import os
import re
from sqlalchemy.exc import IntegrityError


@app.route('/employees', methods=['GET'])
@login_required
def employees():
    employee = Employee.query.all()
    companies = Company.query.all()
    return render_template('employees.html', title = 'Employees', number = len(employee), employee = employee, companies = companies)

@app.route('/add-employee', methods=['POST'])
@login_required
def add_employee():
    name = request.form['employee-name'].capitalize().strip()
    surname = request.form['employee-surname'].capitalize().strip()
    email = request.form['employee-email'].strip()
    phone = request.form['employee-phone']
    mobile_phone = request.form['employee-mphone']
    job = request.form['employee-job']
    company_name = request.form['company-name']

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email) and email != '':
        flash('A valid email is required !', 'error')
        return redirect(url_for('employees'))

    pattern = r'^0\d(\s?\d{2}){4}$'
    if not re.match(pattern, phone) and phone != '':
        flash('A valid phone number is required !', 'error')
        return redirect(url_for('employees'))

    pattern = r'^0\d(\s?\d{2}){4}$'
    if not re.match(pattern, mobile_phone) and mobile_phone != '':
        flash('A valid phone number is required !', 'error')
        return redirect(url_for('employees'))

    try:
        employee = Employee(name = name, surname = surname, email = email, phone = phone, mobile_phone = mobile_phone, job = job, company_name = company_name)
        db.session.add(employee)
        db.session.commit()
    except IntegrityError:
        flash('Employee already registred', 'error')
        return redirect(url_for('employees'))

    flash('Employee has been created', 'success')
    return redirect(url_for('employees'))

@app.route('/edit-employee', methods=['POST'])
@login_required
def edit_employee():
    _id = request.form['edit-employee-id']
    name = request.form['edit-employee-name'].capitalize().strip()
    surname = request.form['edit-employee-surname'].capitalize().strip()
    email = request.form['edit-employee-email'].strip()
    phone = request.form['edit-employee-phone']
    mobile_phone = request.form['edit-employee-mphone']
    job = request.form['edit-employee-job']
    company_name = request.form['edit-employee-company-name']

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email) and email != '':
        flash('A valid email is required !', 'error')
        return redirect(url_for('employees'))

    pattern = r'^0\d(\s?\d{2}){4}$'
    if not re.match(pattern, phone) and phone != '':
        flash('A valid phone number is required !', 'error')
        return redirect(url_for('employees'))

    pattern = r'^0\d(\s?\d{2}){4}$'
    if not re.match(pattern, mobile_phone) and mobile_phone != '':
        flash('A valid phone number is required !', 'error')
        return redirect(url_for('employees'))

    employee = Employee.query.filter_by(id = _id).first()
    employee.name = name
    employee.surname = surname
    employee.email = email
    employee.phone = phone
    employee.mobile_phone = mobile_phone
    employee.job = job
    employee.company_name = company_name
    db.session.commit()
    flash('Employee has been modified', 'success')
    return redirect(url_for('employees'))

@app.route('/remove-employee', methods=['POST'])
@login_required
def remove_employee():
    _id = request.form['rm-employee-id']
    Employee.query.filter_by(id = _id).delete()
    db.session.commit()
    flash('Employee has been removed', 'error')
    return redirect(url_for('employees'))

@app.route('/set-employee-image', methods=['POST'])
@login_required
def employee_image():
    _id = request.form['upload-employee-id']
    employee = Employee.query.filter_by(id = _id).first()
    if "image" in request.files:
        image = request.files["image"]
        image_name = f'{employee.name}.jpg'
        image_path = f'static/img/contacts/{image_name}'
        if os.path.exists(image_path):
            os.remove(image_path)
        images.save(image, name = image_name)
        employee.image = image_name
        db.session.commit()
    return redirect(url_for('employees'))
