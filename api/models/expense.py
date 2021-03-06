from datetime import datetime

from extensions import db
from models.user import User


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

    def __str__(self) -> str:
        return f"{self.user} - {self.figure}"

    @property
    def data(self) -> dict:
        """Serialized data."""
        return {
            'id': self.id,
            'figure': self.figure,
            'user': User.get_username_by_id(self.user),
            'category': self.category,
            'currency': self.currency,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_user(cls, user):
        return cls.query.filter_by(user=user).all()

    @classmethod
    def get_by_category_by_user(cls, user, category):
        return cls.query.filter_by(user=user).filter_by(category=category)

    @classmethod
    def get_by_year(cls, year):
        search_year_start = datetime(year, 1, 1)
        search_year_end = datetime(year+1, 1, 1)
        return cls.query.filter(cls.created_at <= search_year_end).filter(cls.created_at >= search_year_start)

    @classmethod
    def get_by_year_and_month(cls, year, month):
        next_month = 1 if month == 12 else month + 1
        check_year = year+1 if month == 12 else year
        search_year_start = datetime(year, month, 1)
        search_year_end = datetime(check_year, next_month, 1)
        return cls.query.filter(cls.created_at <= search_year_end).filter(cls.created_at >= search_year_start)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
