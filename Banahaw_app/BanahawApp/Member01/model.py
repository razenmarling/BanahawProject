from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Member01


class Member01_data(Mini_func):
	def __init__(self,**kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['member00id']
		self.__data = None

	def getmemberdata(self):

		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,""):
				self.__search_filter.append(getattr(T_Member01,key)==self.__args[key])

		if not self.__search_filter:
			self.__data = self.__session.query(T_Member01).order_by(T_Member01.member00id).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

		else:
			if len(self.__search_filter) != 0:
				self.__data = self.__session.query(T_Member01).filter(*self.__search_filter).order_by(
					T_Member01.member01id).all()

				for d in self.__data:
					r = d.toJSONExcept()
					self._retval.append(r)

	def postmemberdata(self, **kwargs):

		member = T_Member01()

		for key in kwargs:
			try:
				setattr(member,key,kwargs[key])
			except TypeError:
				continue

		self.__session.add(member)

		self.__session.commit()

	def get_customize_members(self, char):
		sel_statement = """SELECT name, membertype, member00id from member00 where name like '%{0}%' union all
						   SELECT name, relationship, member00id from member01 where name like '%{0}%' """.format(char)

		result = self.__session.execute(sel_statement)

		for d in result:
			r = {
				'name': d.name,
				'membertype': d.membertype,
				'member00id': d.member00id
			}
			self._retval.append(r)

	def __del__(self):
		if self.__session is not None:
			self.__session.close()