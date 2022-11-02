from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import Event

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    event = Event.query.all()
    return render_template('index.html', event=event)

@bp.route('/search')
def search():
    if request.args.get('search', False):
        print(request.args['search'])
        even = '%' + request.args['search'] + '%'
        event = Event.query.filter(Event.name.like(even)).all()
        return render_template('index.html', event=event)

    else:
        return redirect(url_for('main.index'))