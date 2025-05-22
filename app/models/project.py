from app.extensions import db

class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    status = db.Column(
        db.Enum('planning', 'in_progress', 'completed', 'cancelled', 'delayed', 'overdue', 'on_hold', 'postponed', name='project_status'),
        default='planning',
        nullable=False
    )
    
    # Foreign key
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    # Relationships
    tasks = db.relationship('Task', back_populates='project', lazy=True)
    team = db.relationship('Team', back_populates='projects')

    # Timestamps
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Project {self.name}>'

    
