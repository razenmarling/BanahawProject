from flask_restful import Resource,reqparse
from .model import Login_data,Login_validation

class Login(Resource):
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()


	def get(self):
		retval = dict()
		status = 200

		args_list = [('username',str,'args',None,False),
		('role',str,'args',None,False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		login = Login_data(**self.__args)

		result = login.get_data()

		retval = result

		return retval,status


	def post(self):
		retval = dict()
		status = 201

		args_list = [('username',str,'json',None,True),
		('password',str,'json',None,True),
		('role',str,'json',None,True)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		login = Login_data()

		login.insert_user(**self.__args)

		result = login.get_data()

		if result['total'] == 0:
			status = 400

		retval = result

		return retval,status

class LoginValidation(Resource):
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		status = 200

		args_list=[('username',str,'args',None,True),
		('password',str,'args',None,True)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		login_val = Login_validation(**self.__args)

		result = login_val.validate()

		retval = result

		# if retval['status'] not in ('OK'):
		# 	status = 400

		return retval,status

