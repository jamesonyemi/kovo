from app.extensions import db

class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)

    # Relationships
    users = db.relationship('User', back_populates='team', cascade='all, delete-orphan')
    projects = db.relationship('Project', back_populates='team', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Team {self.name}>"
