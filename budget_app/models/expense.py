from datetime import date

from extensions import db

expenses = []


class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.Integer(), db.ForeignKey('user.id'))
    figure = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    currency = db.Column(db.String(3), nullable=False, default='GBP')
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    last_updated = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(),
                             onupdate=db.func.now())

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_user(cls, user):
        return cls.query.filter_by(user=user).first()

    @classmethod
    def get_by_category_by_user(cls, user, category):
        return cls.query.filter_by(user=user).filter_by(category=category)

    @classmethod
    def get_by_user_by_figure_gt(cls, user, figure):
        return cls.query.filter_by(user=user).filter_by(figure >= figure)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def data(self) -> dict:
        """Serialized data."""
        return {
            'id': self.id,
            'figure': self.figure,
            'user': self.user,
            'category': self.category,
            'currency': self.currency,
            'created_at': self.created_at.isoformat()
        }

    def __str__(self) -> str:
        return f"{self.date} - {self.figure}"