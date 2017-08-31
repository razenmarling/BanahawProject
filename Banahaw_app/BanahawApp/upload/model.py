"""."""

import os


class Uploadmodel(object):
	"""."""
	def __init__(self, filepath):
		"""."""
		self.__filepath = filepath

	def process_file(self):
		"""."""
		print(os.path.exists(self.__filepath))

	def __check_file_already_uploaded(self):
		"""."""
		pass

