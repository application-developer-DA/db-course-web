__author__ = 'Daniel Abramov'

import pyodbc

from bottle import route, run, debug, template, request


@route('/index')
def main_page():
    return template('auth_form')

debug(True)
run(reloader=True)