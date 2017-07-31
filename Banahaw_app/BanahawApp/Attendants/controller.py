from flask_restful import Resource,reqparse
from .model import Attendants_data

class Attendants(Resource):

	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		services = Attendants_data()
		services.get_attendants()
		result = services.get_data()
		retval = result

		return retval,status

	def post(self):
		status = 201

		args_list = [('hiredate',str,'json',None,False),
					 ('attendant_name',str,'json',None,False),
					 ('allowance',int,'json',None,False),
					 ('mobilenumber',str,'json',None,False),
					 ('position',str,'json',None,False),
					 ('address',str,'json',None,False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		services = Attendants_data()

		services.insert_Attendant(**self.__args)

		return status

	def delete(self):
		status = 204

		args_list = [('attendantid', int, 'args', 'None', True)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()


		services = Attendants_data(**self.__args)
		services.get_attendants()
		result = services.del_attendants()

		return status

	def put(self):
		retval = dict()
		status = 200

		update_args = dict()

		args_update_list = [('attendantid', int, 'json', 'None', True),
							('position', str, 'json', 'None', True),
							('allowance', int, 'json', 'None', True)]

		for args in args_update_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		update_args = self.__reqparser.parse_args()

		services = Attendants_data()
		result = services.edit_attendant(**update_args)

		if result:
			retval['data'] = [{'Message':'Update Complete'}]
		else:
			retval['data'] = [{'Message':'Update Failed'}]

		return retval,status
