from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
     # Foreign key
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    # Relationships
    team = db.relationship('Team', back_populates='users')

    def __repr__(self):
        return f"<User {self.username}>"