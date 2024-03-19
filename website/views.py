from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Course
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #schemat dla notatki
            db.session.add(new_note) #dodowanie notatki
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #schemat dla notatki
            db.session.add(new_note) #dodowanie notatki
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)

@views.route('/courses', methods=['GET'])
@login_required
def courses():
    
    return render_template("courses.html", user=current_user)

@views.route('/courses/<id>', methods=['GET'])
#@token_required
def get_one_courses(id):#current_user, 
    courses = Course.query.filter_by(id=id).first()#, user_id=current_user.id

    if not courses:
        return jsonify({'message' : 'No courses found!'})

    courses_data = {}
    courses_data['id'] = courses.id
    courses_data['description'] = courses.description
    courses_data['title'] = courses.title
    courses_data['complete'] = courses.complete

    return jsonify(courses_data)

@views.route('/courses/<id>', methods=['DELETE'])
#@token_required
def delete_courses(courses_id):#,current_user, 
    courses = Course.query.filter_by(id=id).first()#, , user_id=current_user.id

    if not courses:
        return jsonify({'message' : 'No courses found!'})

    db.session.delete(courses)
    db.session.commit()

    return jsonify({'message' : 'courses item deleted!'})


@views.route('/administration_panel', methods=['GET'])
@login_required
def administration_panel():
    
    return render_template("administration_panel.html", user=current_user)

@views.route('/delete_note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
