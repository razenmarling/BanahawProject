from flask_restful import Resource,reqparse
from .model import Attendant_report, Summary_report, Memberslist_report


class Reporthandler(Resource):
	"""Attendant Report"""
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		args_search_list = [
			('from', str, 'args', None, True),
			('to', str, 'args', None, True),
			('attendantid', int, 'args', None, True)
		]

		for args in args_search_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		search_args = self.__reqparser.parse_args()
		reports = Attendant_report(**search_args)
		result = reports.get_reports_data()

		if result:
			retval = result

		return retval, status

class Reporthandler2(Resource):
	"""Summary Report"""
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		args_search_list = [
			('from', str, 'args', None, True),
			('to', str, 'args', None, True)
		]

		for args in args_search_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		search_args = self.__reqparser.parse_args()
		reports = Summary_report(**search_args)
		result = reports.get_reports_data()

		if result:
			retval = {
				'filename': result
			}

		return retval, status

class Reporthandler3(Resource):
	"""Members List."""
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		args_search_list = [
			('from', str, 'args', None, True),
			('to', str, 'args', None, True)
		]

		for args in args_search_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		search_args = self.__reqparser.parse_args()		
		reports = Memberslist_report(**search_args)
		result = reports.get_reports_data()

		if result:
			retval = {
				'filename': result
			}

		return retval, status
