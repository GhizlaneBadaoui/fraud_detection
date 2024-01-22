# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():
    users = [["oussama307r",True,"bot",60],["oussama",True,"bot",60]]
    return render_template('home/index.html', segment = 'index', users = users)

@blueprint.route('/get')
@login_required
def get_info():
    #url = "http://127.0.0.1:5003/"
    #json_data = request.get_json()
    #likes, botSize, humanSize, users = requests.post(url=url, json=json_data)
    likes, botSize, humanSize, users = (1000,3,4,[["oussama307r",True,"bot",60],["oussama",True,"bot",60]])
    return render_template('home/index.html', humanSize = humanSize, botSize = botSize, Nblikes = likes, users = users)

@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
