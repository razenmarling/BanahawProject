import datetime
from flask_restful import Resource,reqparse
from .model import Attendants01_data

class Attendants01(Resource):
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		args_list = [('from',str,'args',None,False),
					 ('to',str,'args',None,False),
					 ('attendantid',int,'args',None,False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		services = Attendants01_data(**self.__args)
		services.get_rawtime()
		result = services.get_data()
		retval = result

		return retval,status

	def post(self):
		status = 201

		args_list = [('attendantid',int,'json',None,True),
					 ('timein',str,'json',None,False),
					 ('timeout',str,'json',None,False),
					 ('trandate',lambda x: datetime.datetime.strptime(x, '%d-%B-%Y'),'json',datetime.datetime.now().date(),False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		services = Attendants01_data()

		services.insert_rawtime(**self.__args)

		return status
