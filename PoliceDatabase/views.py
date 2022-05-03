"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import Flask, render_template
from PoliceDatabase import app
from PoliceDatabase.models import *
from PoliceDatabase.operations import *

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/police')
def police():
    """Renders the about page."""
    return render_template(
        'police.html',
        title='Police',
        year=datetime.now().year,
        message='Your application description page.',
        Police_Member = Police_Member.query.all()
        )

@app.route('/criminal')
def criminal():
    """Renders the about page."""
    return render_template(
        'criminal.html',
        title='Criminal',
        year=datetime.now().year,
        message='Your application description page.',
        Criminal_Member = Criminal_Member.query.all()
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/patrol')
def patrol():
    """Renders the about page."""
    return render_template(
        'patrol.html',
        title='Patrol',
        year=datetime.now().year,
        message='Your application description page.',
        Patrol = Patrol.query.all()
        )

@app.route('/mandate')
def mandate():
    """Renders the about page."""
    return render_template(
        'mandate.html',
        title='Mandate',
        year=datetime.now().year,
        message='Your application description page.',
        mandates = Crime.query.all()
        )