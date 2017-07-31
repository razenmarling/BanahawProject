from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Add_Ons


class Add_Ons_data(Mini_func):
	def __init__(self,**kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['add_ons_name']
		self.__data = None

	def get_add_ons_data(self):

		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,""):
				self.__search_filter.append(getattr(T_Add_Ons,key)==self.__args[key])

		if len(self.__search_filter) != 0:
			self.__data = self.__session.query(T_Add_Ons).filter(*self.__search_filter).order_by(
				T_Add_Ons.add_ons_id).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)
		else:
			self.__data = self.__session.query(T_Add_Ons).order_by(T_Add_Ons.add_ons_id).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

	def edit_add_ons_data(self, **kwargs):
		update_kwargs = kwargs
		search_param = ['add_ons_id']
		search_filter = list()

		for key in search_param:
			if key in update_kwargs and update_kwargs[key] not in (None,""):
				search_filter.append(getattr(T_Add_Ons, key) == update_kwargs[key])

		if search_filter:
			result = self.__session.query(T_Add_Ons).filter(*search_filter).all()
		else:
			return False

		update_param = ['member_price', 'non_member_price', 'duration']

		for obj in result:
			for key in update_param:
				if key in update_kwargs and update_kwargs[key] not in (None, ""):
					try:
						setattr(obj,key,update_kwargs[key])
					except TypeError:
						continue

		self.__session.commit()

	def del_Add_Ons(self, **kwargs):
		addonid = kwargs.get('id', 0)

		resdata = self.__session.query(T_Add_Ons).filter(T_Add_Ons.add_ons_id == addonid).first()

		if resdata:
			self.__session.delete(resdata)

		try:
			self.__session.commit()
		except:
			self.__session.rollback()

	def insert_add_ons(self, **kwargs):
		addons = T_Add_Ons()

		for key, value in kwargs.items():
			try:
				setattr(addons,key,value)
			except TypeError:
				continue

		self.__session.add(addons)

		self.__session.commit()

	def __del__(self):
		if self.__session is not None:
			self.__session.close()