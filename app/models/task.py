from app.extensions import db
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.Enum('pending', 'in_progress', 'completed', 'cancelled', name='task_status'), default="planning")
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    project = db.relationship('Project', back_populates='tasks', lazy=True)

    def __repr__(self):
        return f'<Task {self.name}>'  