from flask import Blueprint
from flask import render_template

project_bp = Blueprint('project', __name__, url_prefix='/projects', template_folder='templates')

@project_bp.route('/')
def index():
    page_title = 'Projects'
    return render_template('pages/projects/index.html', page_title=page_title)

