from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Healing_Packages


class Healing_Packages_data(Mini_func):
	def __init__(self,**kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['service_name']
		self.__data = None

	def get_healing_packages_data(self):
		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,""):
				self.__search_filter.append(getattr(T_Healing_Packages,key)==self.__args[key])

		if len(self.__search_filter) != 0:
			self.__data = self.__session.query(T_Healing_Packages).filter(*self.__search_filter).order_by(
				T_Healing_Packages.healing_packages_id).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

		else:
			self.__data = self.__session.query(T_Healing_Packages).order_by(T_Healing_Packages.healing_packages_id).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

	def edit_healing_packages_data(self, **kwargs):
		update_kwargs = kwargs
		search_param = ['healing_packages_id']
		search_filter = list()

		for key in search_param:
			if key in update_kwargs and update_kwargs[key] not in (None,""):
				search_filter.append(getattr(T_Healing_Packages, key) == update_kwargs[key])

		if search_filter:
			result = self.__session.query(T_Healing_Packages).filter(*search_filter).all()
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

	def del_healing_packages_data(self, **kwargs):
		"""."""
		retval = True
		hpid = kwargs.get('id', 0)

		result = self.__session.query(T_Healing_Packages).filter(T_Healing_Packages.healing_packages_id == hpid).first()

		if result:
			self.__session.delete(result)
		try:
			self.__session.commit()
		except:
			self.__session.rollback()
			retval = False

		return retval

	def insert_healing_packages_data(self, **kwargs):
		"""."""
		healingpackage = T_Healing_Packages()

		for key, value in kwargs.items():
			try:
				setattr(healingpackage,key,value)
			except TypeError:
				continue

		self.__session.add(healingpackage)

		self.__session.commit()

	def __del__(self):
		if self.__session is not None:
			self.__session.close()