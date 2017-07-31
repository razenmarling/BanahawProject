import datetime
from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Member00


class Member00_data(Mini_func):
	def __init__(self,**kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['member00id', 'membertype','attendantid','upgraded_by']
		self.__data = None

	def getmemberdata(self):

		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,""):
				self.__search_filter.append(getattr(T_Member00,key)==self.__args[key])

		ds = self.__args.get('from', None)
		de = self.__args.get('to', None)
		upg = self.__args.get('upgraded_by', None)

		if ds and de and not upg:
			self.__search_filter.append(getattr(T_Member00,'datecreated').between(ds,de))

		if ds and de and upg:
			self.__search_filter.append(getattr(T_Member00,'upgraded').between(ds,de))			

		if not self.__search_filter:
			self.__data = self.__session.query(T_Member00).order_by(T_Member00.member00id).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

		else:
			self.__data = self.__session.query(T_Member00).filter(*self.__search_filter).order_by(
				T_Member00.member00id).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

	def postmemberdata(self, **kwargs):

		member = T_Member00()

		for key in kwargs:
			try:
				setattr(member,key,kwargs[key])
			except TypeError:
				continue

		self.__session.add(member)

		self.__session.commit()

		query = "select max(member00id) from member00;"
		result = self.__session.execute(query).first()

		for memid in result:
			r = {'member00id':memid}
			self._retval.append(r)

	def editmemberdata(self, **kwargs):
		update_kwargs = kwargs
		search_param = ['member00id']
		search_filter = list()
		retval = False

		for key in search_param:
			if key in update_kwargs and update_kwargs[key] not in (None,""):
				search_filter.append(getattr(T_Member00, key) == update_kwargs[key])

		if search_filter:
			retval = True
			data = self.__session.query(T_Member00).filter(*search_filter).order_by(
				T_Member00.member00id).all()

		update_param = ['membershipcost', 'membertype', 
						'upgraded_by', 'upgraded', 'address',
						'mobile_number', 'landline_number', 'email_address',
						'birthdate', 'name']

		print(update_kwargs)
		for obj in data:
			for key in update_param:
				if key in update_kwargs and update_kwargs[key] not in (None,""):
					if key == 'upgraded':
						print('upgraded')
						update_kwargs[key] = datetime.datetime.strptime(update_kwargs[key], '%m/%d/%Y')
						print(update_kwargs[key])
					try:
						setattr(obj,key,update_kwargs[key])
					except TypeError:
						continue

		self.__session.commit()

		return retval

	def get_customize_members(self, char):
		memtype = self.__args.get('membertype', None)

		result = self.__session.query(T_Member00).filter(T_Member00.name.like("%{}%".format(char))
			).filter(T_Member00.membertype=="{}".format(memtype)).all()

		for d in result:
			r = d.toJSONExcept()
			print(r)
			self._retval.append(r)

	def __del__(self):
		if self.__session is not None:
			self.__session.close()