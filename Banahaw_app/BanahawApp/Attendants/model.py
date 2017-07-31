from sqlalchemy import and_
from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Attendants


class Attendants_data(Mini_func):
	def __init__(self, **kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['attendant_name', 'attendantid']
		self.__data = None

	def get_attendants(self):

		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,""):
				self.__search_filter.append(getattr(T_Attendants,key)==self.__args[key])

		if not self.__search_filter:
			self.__data = self.__session.query(T_Attendants).order_by(T_Attendants.attendantid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

		else:
			self.__data = self.__session.query(T_Attendants).filter(*self.__search_filter).order_by(
				T_Attendants.attendantid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

	def del_attendants(self):
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

	def insert_Attendant(self,**kwargs):
		attendant = T_Attendants()

		for key in kwargs:
			try:
				setattr(attendant,key,kwargs[key])
			except TypeError:
				continue

		self.__session.add(attendant)

		self.__session.commit()

	def edit_attendant(self,**kwargs):
		update_kwargs = kwargs
		search_param = ['attendantid']
		search_filter = list()

		for key in search_param:
			if key in update_kwargs and update_kwargs[key] not in (None,''):
				search_filter.append(getattr(T_Attendants,key)==update_kwargs[key])

		if search_filter:
			retval = True
			self.__data = self.__session.query(T_Attendants).filter(
				and_(*search_filter)).order_by(T_Attendants.attendantid).all()
		else:
			retval = False

		update_list = ['position', 'allowance']
		for obj in self.__data:
			for key in update_list:
				if key in update_kwargs and update_kwargs[key] not in ('',None):
					try:
						setattr(obj,key,update_kwargs[key])
					except TypeError:
						continue

		self.__session.commit()


	def __del__(self):
		if self.__session is not None:
			self.__session.close()