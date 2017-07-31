from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Products


class Product_data(Mini_func):
	def __init__(self):
		self.__session = Session()

	def purchase_product(self, **kwargs):
		prod = T_Products()

		for key in kwargs:
			try:
				setattr(prod,key,kwargs[key])
			except TypeError:
				continue

		self.__session.add(prod)

		self.__session.commit()


