from PoliceDatabase import app, db
from PoliceDatabase.models import *
from flask import Flask, render_template, request, flash, url_for, redirect

#################################################################################################################################################
##########################################################||POLICE OPERATIONS||##################################################################
#################################################################################################################################################

@app.route('/add_police', methods = ['GET', 'POST'])
def add_police():
    if request.method == 'POST':
        if not request.form['phone'] or not request.form['city'] or \
           not request.form['adress'] or not request.form['name'] or \
           not request.form['surname']:
                flash('Please enter all the fields', 'error')
        else:
            policeman = Police_Member(request.form['phone'], request.form['city'],
                                request.form['adress'], request.form['name'],
                                request.form['surname'], request.form['car_num'],
                                request.form['pol_station'], request.form['rank'])
            db.session.add(policeman)
            db.session.commit()
   
            return redirect(url_for('police'))
    return render_template('add_police.html',
                           Police_Car = Police_Car.query.all(),
                           Police_Station = Police_Station.query.all(),
                           Rank = Rank.query.all())

@app.route("/delete_police", methods=['POST'])
def delete_police():
    id_policja = request.form.get("id_policja")
    policeman = Police_Member.query.filter_by(id_policja=id_policja).first()
    
    db.session.delete(policeman)
    db.session.commit()
    
    return redirect(url_for('police'))


@app.route("/add_patrol", methods = ['GET', 'POST'])
def add_patrol():
    if request.method == 'POST':
        if not request.form['place']:
            flash('Please enter all the fields', 'error')
        else:
            patrol = Patrol(request.form['police_car'],request.form['place'])

            db.session.add(patrol)
            db.session.commit()

            return redirect(url_for('patrol'))
    return render_template('add_patrol.html',
                           Police_Car = Police_Car.query.all()
                           )
    
@app.route("/delete_patrol", methods=['POST'])
def delete_patrol():
    id_patrol = request.form.get("id_patrol")
    patrol = Patrol.query.filter_by(id_patrol=id_patrol).first()
    
    db.session.delete(patrol)
    db.session.commit()
    
    return redirect(url_for('patrol'))

#################################################################################################################################################
##########################################################||CRRIME OPERATIONS||##################################################################
#################################################################################################################################################

@app.route('/add_criminal', methods = ['GET', 'POST'])
def add_criminal():
    if request.method == 'POST':
        if not request.form['phone'] or not request.form['city'] or \
           not request.form['adress'] or not request.form['name'] or \
           not request.form['surname']:
                flash('Please enter all the fields', 'error')
        else:
            crimeman = Criminal_Member(request.form['name'], request.form['surname'],
                                request.form['phone'], request.form['city'],
                                request.form['adress'])
            db.session.add(crimeman)
            db.session.commit()
   
            return redirect(url_for('criminal'))
    return render_template('add_criminal.html')

@app.route("/delete_criminal", methods=['POST'])
def delete_criminal():
    id_przestepcy = request.form.get("id_przestepcy")
    crimeman = Criminal_Member.query.filter_by(id_przestepcy=id_przestepcy).first()
    
    db.session.delete(crimeman)
    db.session.commit()
    
    return redirect(url_for('criminal'))

@app.route("/modify_criminal", methods=['GET' ,'POST'])
def modify_criminal():
    id_przestepcy = request.form.get("id_przestepcy")
    return render_template('modify_criminal.html',
                            Criminal_Member = Criminal_Member.query.filter_by(id_przestepcy=id_przestepcy)
                            )

@app.route("/add_mandate", methods=['GET', 'POST'])
def add_mandate():
    if request.method == 'POST':
          if not request.form['data']:
                flash('Please enter all the fields', 'error')
          else:
                mandate = Crime(request.form['criminal_member'], request.form['police_member'] ,
                                request.form['type_crime'], request.form['data'])
                db.session.add(mandate)
                db.session.commit()
   
          return redirect(url_for('criminal'))
    
    return render_template('add_mandate.html',
                           Type_of_criminal = Type_of_criminal.query.all(),
                           Criminal_Member = Criminal_Member.query.all(),
                           Police_Member = Police_Member.query.all()
                           )

@app.route("/delete_mandate", methods=['POST'])
def delete_mandate():
    id_mandat = request.form.get("id_przestepstwa")
    mandat = Crime.query.filter_by(id_przestepstwa=id_mandat).first()
    
    db.session.delete(mandat)
    db.session.commit()

    return redirect(url_for('mandate'))