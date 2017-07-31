import datetime
from flask_restful import Resource, reqparse
from .model import Promomodel


class Promohandler(Resource):
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = list()
		status = 200

		args_list = [('active', bool, 'args', None, False),
					 ('curdate', bool, 'args', None, False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		promos = Promomodel(**self.__args)
		result = promos.get_promo()

		if result:
			retval = result

		return retval, status

	def post(self):
		status = 201

		args_list = [('description', str, 'json', None, False),
					 ('member_price', str, 'json', None, False),
					 ('non_member_price', str, 'json', None, False),
					 ('duration', int, 'json', None, False),
					 ('datestart', lambda x: datetime.datetime.strptime(x, '%d-%B-%Y'), 'json', None, False),
					 ('dateend', lambda x: datetime.datetime.strptime(x, '%d-%B-%Y'), 'json', None, False),
					 ('active', bool, 'json', True, False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		promos = Promomodel(**self.__args)
		promos.make_promo()

		return status

	def put(self):
		retval = None
		status = 200

		args_list = [('promoid', str, 'json', None, True),
					 ('member_price', str, 'json', None, False),
					 ('non_member_price', str, 'json', None, False),
					 ('duration', str, 'json', None, False),
					 ('datestart', str, 'json', None, False),
					 ('dateend', str, 'json', None, False),
					 ('active', bool, 'json', None, False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		promos = Promomodel(**self.__args)
		result = promos.edit_promo()

		if result:
			retval = result

		return retval

	def delete(self):
		pass
