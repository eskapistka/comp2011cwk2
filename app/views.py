from flask import render_template, flash, request, redirect, url_for
from flask import Blueprint
from flask_login import login_required, current_user
from app import app, models
#from .forms import AssessmentForm
from app import db

app = Blueprint('app', __name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                           name=current_user.name)



"""
@app.route('/all', methods=['GET', 'POST'])
def all():
    form = AssessmentForm()

    # adding to the database on form submission
    if form.validate_on_submit():
        record = models.Assessment(title=form.title.data,
                                   code=form.code.data,
                                   deadline=form.deadline.data,
                                   description=form.description.data)

        db.session.add(record)
        db.session.commit()

    assessments = models.Assessment.query.all()

    return render_template('old/all.html',
                           title='my assessment board - all',
                           form=form,
                           assessments=assessments,
                           subpagetitle='all')

@app.route('/done', methods=['GET'])
def done():
    complete = models.Assessment.query.filter_by(complete=True).all()

    return render_template('old/done.html',
                           title='my assessment board - done',
                           assessments=complete,
                           subpagetitle='done')

@app.route('/todo', methods=['GET'])
def todo():
    incomplete = models.Assessment.query.filter_by(complete=False).all()

    return render_template('old/todo.html',
                           title='my assessment board - to-do',
                           assessments=incomplete,
                           subpagetitle='todo')

@app.route('/delete/<id>')
def delete(id):
    toDelete = models.Assessment.query.filter_by(id=int(id)).first()

    db.session.delete(toDelete)
    db.session.commit()

    return redirect(url_for('all'))

@app.route('/togglestate/<id>')
def toggleState(id):
    state = models.Assessment.query.filter_by(id=int(id)).first()

    state.complete = not state.complete
    db.session.commit()

    return redirect(url_for('all'))

"""