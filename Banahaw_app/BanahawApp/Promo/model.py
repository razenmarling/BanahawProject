import datetime
from sqlalchemy import and_
from BanahawApp import Session,Mini_func
from BanahawApp.table import T_promos


class Promomodel(object):
	def __init__(self, **kwargs):
		self.__session = Session()
		self.__kwargs = kwargs

	def make_promo(self):
		promo = T_promos()

		for key, value in self.__kwargs.items():

			if value:
				if key in ('datestart', 'dateend'):
					value = value.strftime('%Y-%m-%d')

				setattr(promo, key, value)

		self.__session.add(promo)

		self.__session.commit()

	def get_promo(self):
		retval = list()
		search_filter = list()

		for key, value in self.__kwargs.items():
			if key in ('curdate') and value:
				datetoday = datetime.datetime.now().date().strftime('%Y-%m-%d')
				search_filter.append(getattr(T_promos, 'datestart') <= datetoday)
				search_filter.append(getattr(T_promos, 'dateend') >= datetoday)
			else:
				if value:
					search_filter.append(getattr(T_promos, key) == value)

		if search_filter:
			result = self.__session.query(T_promos).filter(and_(*search_filter)).all()

			for data in result:
				dict_data = data.toJSONExcept()
				retval.append(dict_data)

		else:
			result = self.__session.query(T_promos).all()

			for data in result:
				dict_data = data.toJSONExcept()
				retval.append(dict_data)

		return retval

	def edit_promo(self):
		retval = None

		promoid = self.__kwargs.get('promoid', 0)

		if not promoid:
			return retval

		promoobj = self.__session.query(T_promos).filter(
						getattr(T_promos, 'promoid') == promoid).first()

		for key, value in self.__kwargs.items():

			if value in ('', None):
				continue

			if key in ('datestart', 'dateend'):
				dateval = datetime.datetime.strptime(value, '%m/%d/%Y')
				value = dateval.strftime('%Y-%m-%d')

			setattr(promoobj, key, value)

		try:
			self.__session.commit()
		except:
			retval = None
		else:
			retval = self.__kwargs

		return retval
