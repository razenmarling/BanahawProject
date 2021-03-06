from flask_restful import Resource, reqparse
from .model import Product_data


class Producthandler(Resource):

	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def post(self):
		status = 200

		args_list = [('productname',str,'json',None,True),
					 ('customername',str,'json',None,True),
					 ('amountpaid',int,'json',None,True)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		prod = Product_data()
		prod.purchase_product(**self.__args)

		return status

	def get(self):
		status = 200
		retval = dict()

		args_list = [('from', str, 'args', None, False),
					 ('to', str, 'args', None, False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		prod = Product_data()
		prod.get_product(**self.__args)

		result = prod.get_data()
		retval = result

		return retval, status
