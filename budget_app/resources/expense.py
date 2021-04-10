from datetime import date

from flask_restful import Resource
from flask import request

from models.expense import Expense
from http import HTTPStatus


class ExpenseListResource(Resource):
    """Resource which provides 2 endpoints:
        - GET (list all created expenses within database)
        - POST (create new expense object and save it to database)
    """
    def get(self):
        expenses = Expense.get_all()
        data = [expense.data for expense in expenses]
        return {'expenses': data}, HTTPStatus.OK

    def post(self):
        """Example of JSON request body:
            {
                "figure": 123,
                "user": 2,
                "category": "Food",
                "currency": "PLN",
                "created_at": "2021-01-12"
            }
        """
        data = request.get_json()

        # Check if date has a correct ISO format:
        try:
            date_from_iso = date.fromisoformat(data['created_at'])
        except ValueError:
            return {'message': 'Incorrect date format. Must be in ISO format YYYY-MM-DD.'}, HTTPStatus.BAD_REQUEST

        if {'figure', 'user', 'category', 'currency', 'created_at'} == data.keys():
            figure = float(data['figure']) if isinstance(data['figure'], int) else data['figure']
            try:
                figure = round(figure, 2)
            except TypeError:
                return {'message': 'Incorrect data type. Figure must be a number.'}, HTTPStatus.BAD_REQUEST

            expense = self.create_expense(figure=figure,
                                          user=data['user'],
                                          category=data['category'],
                                          currency=data['currency'],
                                          date=date_from_iso
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
        expense.save()
        return expense


class ExpenseResource(Resource):
    """Resource which provides 2 endpoints:
        - GET (return expense with specify ID)
        - DELETE (delete expense objects from database)
    """
    def get(self, id):
        expense = Expense.get_by_id(id)
        if expense:
            return {'book': expense.data}, HTTPStatus.OK
        else:
            return {'message': 'Expense with specify ID not found.'}, HTTPStatus.NOT_FOUND

    def delete(self, id):
        expense = Expense.get_by_id(id)
        if expense:
            expense.delete()
            return {'message': f'Expense with ID {id} has been deleted.'}, HTTPStatus.OK
        else:
            return {'message': 'Expense with specify ID not found.'}, HTTPStatus.NOT_FOUND


class ExpenseYearFilterResource(Resource):
    """RESTful resource for dealing with year filtering. Provide GET endpoint.
    """
    def get(self, year):
        expenses = Expense.get_by_year(year)
        data = [expense.data for expense in expenses]
        return {'expenses': data}, HTTPStatus.OK


class ExpenseMonthFilterResource(Resource):
    """RESTful resource for dealing with year and month filtering. Provide GET endpoint."""
    def get(self, year, month):
        expenses = Expense.get_by_year_and_month(year, month)
        data = [expense.data for expense in expenses]
        return {'expenses': data}, HTTPStatus.OK
