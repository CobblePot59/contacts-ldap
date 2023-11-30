from flask import render_template, request, redirect, url_for, session, flash
from app import app, ldap

from routes.company import *
from routes.employee import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('status'):
        return redirect(url_for('companies'))

    if request.method == 'GET':
       return render_template('login.html')

    username = request.form['username']
    password = request.form['password']
    if str(ldap.authenticate(username+'@'+app.config['LDAP_DOMAIN'], password).status) == 'AuthenticationResponseStatus.success':
        session.update({'status':True, 'username': username})
        return redirect(url_for('companies'))
    else:
        flash('Bad Login', 'error')
        return redirect(url_for('login'))

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login'))
