from datetime import date

from flask_restful import Resource
from flask import request

from models.expense import Expense, expenses
from http import HTTPStatus


class ExpenseListResource(Resource):

    def get(self):
        expenses_data = [expense.data for expense in expenses]
        return {'expenses': expenses_data}, HTTPStatus.OK

    # TODO: walidować czy dane mają poprawny format - figure INT a reszta str.
    def post(self):
        """Example of JSON requests for creating expense:
            {
                "figure": 123,
                "user": "Matjusz",
                "category": "Food",
            }
        OPTIONAL data can be added if needed:
            {
                "currency": "PLN",
                "date": "2021-01-12"
            }
        """
        data = request.get_json()

        # Check if date has a correct ISO format:
        if 'date' in data.keys():
            try:
                date_from_iso = date.fromisoformat(data['date'])
            except ValueError:
                return {'message': 'Incorrect date format. Must be in ISO format YYYY-MM-DD.'}, HTTPStatus.BAD_REQUEST

            if {'figure', 'user', 'category', 'currency', 'date'} == data.keys():
                expense = self.create_expense(figure=data['figure'],
                                              user=data['user'],
                                              category=data['category'],
                                              currency=data['currency'],
                                              date=date_from_iso
                                              )
                return {'expense': expense.data}, HTTPStatus.CREATED

            elif {'figure', 'user', 'category', 'date'} == data.keys():
                expense = self.create_expense(figure=data['figure'],
                                              user=data['user'],
                                              category=data['category'],
                                              date=date_from_iso,
                                              )
                return {'expense': expense.data}, HTTPStatus.CREATED

        if {'figure', 'user', 'category', 'currency'} == data.keys():
            expense = self.create_expense(figure=data['figure'],
                                          user=data['user'],
                                          category=data['category'],
                                          currency=data['currency']
                                          )
            return {'expense': expense.data}, HTTPStatus.CREATED

        elif {'figure', 'user', 'category'} == data.keys():
            expense = self.create_expense(figure=data['figure'],
                                          user=data['user'],
                                          category=data['category']
                                          )
            return {'expense': expense.data}, HTTPStatus.CREATED

        else:
            return {'message': 'Incomplete data.'}, HTTPStatus.BAD_REQUEST

    @staticmethod
    def create_expense(figure, user, category, currency="GBP", date=date.today()):
        """Function create an Expense object and save it to database."""
        expense = Expense(
            figure=figure,
            user=user,
            category=category,
            currency=currency,
            created_at=date
        )
        expenses.append(expense)
        return expense


class ExpenseYearFilterResource(Resource):
    """RESTful resource for dealing with year filtering."""

    def get(self, year):
        expenses_data = [expense.data for expense in expenses if expense.date.year == year]
        return {'expenses': expenses_data}, HTTPStatus.OK


class ExpenseMonthFilterResource(Resource):
    """RESTful resource for dealing with year and month filtering."""

    def get(self, year, month):
        expenses_data = [expense.data for expense in expenses if
                         expense.date.month == month and expense.date.year == year]
        return {'expenses': expenses_data}, HTTPStatus.OK

# currency filter??
