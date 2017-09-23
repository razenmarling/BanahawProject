"""Controller."""
from .model import Uploadmodel
from flask_restful import Resource, reqparse
import werkzeug
import os


class Uploadhandler(Resource):
	"""."""

	def __init__(self):
		"""."""
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def post(self):
		"""Post."""
		status = 201
		UPLOADED_PATH = os.getcwd() + '/Upload'

		if not os.path.isdir(UPLOADED_PATH):
			os.makedirs(UPLOADED_PATH)

		self.__reqparser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
		self.__args = self.__reqparser.parse_args()

		file = self.__args.get('file')
		
		if not file:
			status = 404
			return {'Messsage': 'File Not Found'}, status

		file_path = os.path.join(UPLOADED_PATH, file.filename)

		if not os.path.exists(file_path):

			try:
				file.save(file_path)
			except:
				status = 500
				return {'Message': 'Error on Saving File'}, status
			else:
				um = Uploadmodel(file_path, file.filename)
				um.process_file()

		else:
			status = 409
			return {'Message': 'File Already Exist'}, status

		return {'Message':'Success'}, status

