import datetime
from sqlalchemy import and_,desc
from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Reservation


class Reservations_data(Mini_func):
	def __init__(self, **kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['reservationid']
		self.__data = None

	def get_reservations(self):
		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,""):
				self.__search_filter.append(getattr(T_Reservation,key) == self.__args[key])

		ds = self.__args.get('from', None)
		de = self.__args.get('to', None)

		if ds and de:
			self.__search_filter.append(getattr(T_Reservation,'res_date').between(ds,de))

		if self.__search_filter:
			self.__data = self.__session.query(T_Reservation).filter(
				and_(*self.__search_filter)).order_by(T_Reservation.reservationid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

		else:
			self.__data = self.__session.query(T_Reservation).order_by(T_Reservation.reservationid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)


	def post_reservations(self):
		
		reservation = T_Reservation()

		for key in self.__args:
			try:
				setattr(reservation, key, self.__args[key])
			except TypeError:
				continue

		self.__session.add(reservation)

		self.__session.commit()


	def put_reservations(self):
		pass

	def del_reservations(self):
		retval = False

		if self.__data:
			retval = True
			for data in self.__data:
				self.__session.delete(data)

		try:
			self.__session.commit()
		except:
			self.__session.rollback()

		return retval