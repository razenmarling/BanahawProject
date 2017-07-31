import datetime
from sqlalchemy import and_
from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Attendants01


class Attendants01_data(Mini_func):
	def __init__(self, **kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['attendantid']
		self.__data = None

	def get_rawtime(self):
		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,''):
				self.__search_filter.append(getattr(T_Attendants01, key) == self.__args[key])

		ds = self.__args.get('from',None)
		de = self.__args.get('to',None)

		if ds and de:
			self.__search_filter.append(getattr(T_Attendants01,'trandate').between(ds,de))

		if self.__search_filter:

			self.__data = self.__session.query(T_Attendants01).filter(*self.__search_filter).order_by(
				T_Attendants01.attendantid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

		else:
			self.__data = self.__session.query(T_Attendants01).order_by(T_Attendants01.attendantid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

	def insert_rawtime(self, **kwargs):
		attendant = T_Attendants01()

		attendantid = kwargs.get('attendantid', 0)
		trandate = kwargs.get('trandate', 0)
		print(attendantid, trandate)
		att_filter = [getattr(T_Attendants01, 'attendantid') == attendantid,
					  getattr(T_Attendants01, 'trandate') == trandate]

		if not attendantid or not trandate:
			return None

		exist = self.__session.query(T_Attendants01).filter(*att_filter).first()
		
		if not exist:

			for key in kwargs:
				if kwargs[key]:
					try:
						setattr(attendant,key,kwargs[key])
					except TypeError:
						continue

			self.__session.add(attendant)

			self.__session.commit()

		else:
			update_list = ['timein', 'timeout']

			for key in update_list:
				if key in kwargs and kwargs[key]:
					try:
						setattr(exist,key,kwargs[key])
					except TypeError:
						continue

			self.__session.commit()
