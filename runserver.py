"""
This script runs the PoliceDatabase application using a development server.
"""

from os import environ
from PoliceDatabase import app, db

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    db.create_all()
    db.session.commit()
    app.run(HOST, PORT)
