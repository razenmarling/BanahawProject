"""Controller."""
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

		self.__reqparser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
		self.__args = self.__reqparser.parse_args()

		file = self.__args.get('file')
		
		if not file:
			status = 404
			return {'Messsage': 'File Not Found'}, status

		file.save(os.path.join(UPLOADED_PATH, file.filename))

		return status

