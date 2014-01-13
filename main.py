__author__ = 'Daniel Abramov'

import pyodbc

from bottle import route, run, debug, template, request


@route('/index')
def main_page():
    return template('auth_form')

@route('/login', method='POST')
def login():
    host = request.forms.get('host')
    username = request.forms.get('username')
    password = request.forms.get('password')

    connection_string = 'DRIVER={SQL Server};SERVER=%s;DATABASE=SportInfrastructure;UID=%s;PWD=%s' % (host, username, password)

    try:
        connection = pyodbc.connect(connection_string)
    except:
        return 'Error'

    return 'OK'

debug(True)
run(reloader=True)