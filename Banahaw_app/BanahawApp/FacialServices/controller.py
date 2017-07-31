from flask_restful import Resource, reqparse
from .model import Facialmodel


class Facialhandler(Resource):
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		service = Facialmodel()
		result = service.get_services()

		if result:
			retval = result

		return retval, status

	def post(self):
		status = 200

		args_insert_list = [
			('facial_services_name', str, 'json', None, True),
			('member_price', int, 'json', None, True),
			('non_member_price', int, 'json', None, True),
			('duration', int, 'json', None, True)
		]

		for args in args_insert_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		insert_args = self.__reqparser.parse_args()

		service = Facialmodel()
		result = service.insert_facial_service(**insert_args)

		return status

	def delete(self):
		status = 200

		self.__reqparser.add_argument('id', type=int, location='args', default=0, required=True)

		fsid = self.__reqparser.parse_args()
		service = Facialmodel()
		service.del_facial_service(**fsid)

		return status

	def put(self):
		status = 200

		args_update_list = [
			('facial_services_id', int, 'json', None, True),
			('member_price', int, 'json', None, False),
			('non_member_price', int, 'json', None, False),
			('duration', int, 'json', None, False)
		]

		for args in args_update_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		update_args = self.__reqparser.parse_args()
		service = Facialmodel()
		service.edit_facial_services(**update_args)

		return status
