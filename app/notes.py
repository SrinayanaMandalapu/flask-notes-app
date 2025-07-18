from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

notes = Blueprint('notes', __name__)

@notes.route('/notes')
@login_required
def view_notes():
    return render_template('notes.html', notes=current_user.notes)

@notes.route('/notes/add', methods=['POST'])
@login_required
def add_note():
    content = request.form.get('content')
    if content:
        new_note = Note(content=content, author=current_user)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('notes.view_notes'))

@notes.route('/notes/delete/<int:id>')
@login_required
def delete_note(id):
    note = Note.query.get_or_404(id)
    if note.author == current_user:
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for('notes.view_notes'))