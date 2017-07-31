from flask_restful import Resource,reqparse
from .model import Member00_data

class Member00(Resource):

	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self, char=None):
		retval = dict()
		status = 200

		args_list = [('member00id', str, 'args', None, False),
					 ('membertype', str, 'args', None, False),
					 ('from', str, 'args', None, False),
					 ('to', str, 'args', None, False),
					 ('attendantid', str, 'args', None, False),
					 ('upgraded_by', int, 'args', None, False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()


		members = Member00_data(**self.__args)
		if char:
			members.get_customize_members(char)
		else:
			members.getmemberdata()

		result = members.get_data()
		retval = result

		return retval,status

	def post(self):
		retval = dict()
		status = 201

		args_list = [('address', str, 'json', None, False),
					 ('mobile_number', str, 'json', None, False),
					 ('landline_number', str, 'json', None, False),
					 ('email_address', str, 'json', None, False),
					 ('birthdate', str, 'json', None, False),
					 ('membertype', str, 'json', None, False),
					 ('feedback', str, 'json', None, False),
					 ('name', str, 'json', None, False),
					 ('membershipcost', int, 'json', None, False),
					 ('attendant_name', str, 'json', None, False),
					 ('attendantid', int, 'json', None, False),
					 ('datecreated', str, 'json', None, False),
					 ('branch', str, 'json', 'Plaridel', False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		members = Member00_data()
		members.postmemberdata(**self.__args)
		retval = members.get_data()

		return retval, status

	def put(self):
		retval = dict()
		status = 200

		args_list = [('membershipcost', str, 'json', None, False),
					 ('membertype', str, 'json', None, False),
					 ('member00id', str, 'json', None, False),
					 ('upgraded', str, 'json', None, False),
					 ('upgraded_by', int, 'json', None, False),
					 ('address', str, 'json', None, False),
 					 ('mobile_number', str, 'json', None, False),
					 ('landline_number', str, 'json', None, False),
					 ('email_address', str, 'json', None, False),
					 ('birthdate', str, 'json', None, False),
					 ('name', str, 'json', None, False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		members = Member00_data()
		result = members.editmemberdata(**self.__args)

		if not result:
			status = 400

		return status
