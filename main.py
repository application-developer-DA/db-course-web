__author__ = 'Daniel Abramov'

import pyodbc

from bottle import route, run, debug, template, request, static_file, redirect

connection = None

@route('/login', method='GET')
def login_form():
    return template('auth_form')

@route('/bootstrap/<filepath:path>')
def file_get(filepath):
    return static_file(filepath, root='bootstrap')

@route('/login', method='POST')
def login():
    host = request.forms.get('host')
    username = request.forms.get('username')
    password = request.forms.get('password')

    connection_string = 'DRIVER={SQL Server};SERVER=%s;DATABASE=SportInfrastructure;UID=%s;PWD=%s' % (host, username, password)
    try:
        global connection
        connection = pyodbc.connect(connection_string)
    except:
        return 'Error'

    redirect('main_page/Home')

queries = {
    'AllCompetitions' : "SELECT [Competition Name], [Competition Date], [Sport Name], [Building Name], [Organization Name] FROM AllCompetitions",
    'SportsmenWithSports' : "SELECT [Firstname] + ' ' + [Lastname] + ' ' + [Middlename] AS Name, [Birthdate], [Sport], [Title] FROM SportsmenWithSports",
    'SportsmenWithCoaches' : "SELECT [Learner Firstname] + ' ' + [Learner Lastname] + ' ' + [Learner Middlename] AS [Learner Name], [Coach Firstname] + ' ' + [Coach Lastname] + ' ' + [Coach Middlename] AS [Coach Name], [Sport] FROM SportsmenWithCoaches",
    'AllParticipants' : "SELECT [Firstname] + ' ' + [Lastname] + ' ' + [Middlename] AS Name, [Scores], [Club], [Competition Name], [Competiton Date] FROM AllParticipants"
}

@route('/main_page/<name>')
def chosen_page(name):
    if name == 'Home':
        return template('main_page', page=name, rows=None)

    cursor = connection.cursor()
    query = queries[name]
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    return template('main_page', page=name, rows=rows, columns=columns)

debug(True)
run(reloader=True)