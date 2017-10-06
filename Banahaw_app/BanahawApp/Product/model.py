from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Products


class Product_data(Mini_func):
	def __init__(self):
		self.__session = Session()
		self._retval = []

	def purchase_product(self, **kwargs):
		prod = T_Products()

		for key in kwargs:
			try:
				setattr(prod,key,kwargs[key])
			except TypeError:
				continue

		self.__session.add(prod)

		self.__session.commit()

	def get_product(self, **kwargs):
		ds = kwargs.get('from', None)
		de = kwargs.get('to', None)
		search_filter = []

		if ds and de:
			search_filter.append(getattr(T_Products,'datepurchased').between(ds,de))

			data = self.__session.query(T_Products).filter(*search_filter).order_by(
					T_Products.datepurchased).all()

			for d in data:
				r = d.toJSONExcept()
				self._retval.append(r)
