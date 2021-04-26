from extensions import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    last_updated = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    expenses = db.relationship('Expense', backref='_user')

    @classmethod
    def get_username_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        return user.username

    @classmethod
    def get_user_by_username(cls, username):

        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
