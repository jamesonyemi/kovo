from flask import Blueprint

project_bp = Blueprint('project', __name__)

@project_bp.route('/')
def index():
    return '<h1>Project routes</h1>'