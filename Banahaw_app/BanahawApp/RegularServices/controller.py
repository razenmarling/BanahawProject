from flask_restful import Resource,reqparse
from .model import Regular_Services_data

class RegularServices(Resource):

	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		services = Regular_Services_data()
		services.get_regular_services_data()
		result = services.get_data()
		retval = result

		return retval,status

	def post(self):
		status = 200

		args_insert_list = [
			('service_name', str, 'json', None, True),
			('off_peak_price', int, 'json', None, True),
			('peak_price', int, 'json', None, True),
			('non_member_price', int, 'json', None, True),
			('duration', int, 'json', None, True)
		]

		for args in args_insert_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		insert_args = self.__reqparser.parse_args()
		services = Regular_Services_data()
		services.insert_regular_services_data(**insert_args)

		return status

	def put(self):
		status = 200

		update_args = dict()
		args_update_list = [
			('regular_services_id', int, 'json', None, True),
			('off_peak_price', int, 'json', None, False),
			('peak_price', int, 'json', None, False),
			('non_member_price', int, 'json', None, False),
			('duration', int, 'json', None, False)
		]

		for args in args_update_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		update_args = self.__reqparser.parse_args()
		services = Regular_Services_data()
		services.edit_regular_services_data(**update_args)

		return status

	def delete(self):
		status = 200

		self.__reqparser.add_argument('id', type=int, location='args', default=0, required=True)

		regid = self.__reqparser.parse_args()
		services = Regular_Services_data()
		services.del_regular_services_data(**regid)

		return status
