# INTENTIONALLY INSECURE - demo for CodeQL. DO NOT MERGE, DO NOT DEPLOY.
import os
import subprocess

from flask import request, make_response

from server.webapp import flaskapp


@flaskapp.route('/hello')
def hello():
    # Reflected XSS (CWE-079)
    return make_response("<h1>Hello " + request.args.get('who', '') + "</h1>")


@flaskapp.route('/file')
def read_file():
    # Path traversal (CWE-022)
    path = os.path.join('uploads', request.args.get('f', ''))
    return open(path).read()


@flaskapp.route('/ping')
def ping():
    # Command injection (CWE-078)
    host = request.args.get('host', '')
    return subprocess.check_output("ping -c 1 " + host, shell=True)


if __name__ == '__main__':
    # Flask debug mode enabled (CWE-094)
    flaskapp.run(debug=True)
