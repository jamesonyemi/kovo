from flask import Blueprint, render_template, request, redirect, url_for
# from flask_login import login_required, current_user
from app.models import User, Team, Project
from app.forms.team_form import TeamForm
from app.forms.project_form import ProjectForm

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
# @login_required
def index():
    teams = Team.query.all() or []
    projects = Project.query.all() or []
    return render_template('admin/index.html', teams=teams, projects=projects)

