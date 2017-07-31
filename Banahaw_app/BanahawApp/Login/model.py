from BanahawApp import Session,Mini_func,http_session
from BanahawApp.table import Users_table
import bcrypt

class Login_data(Mini_func,object):
	def __init__(self,**kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['username','password','role']
		self.__data = None

		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,''):
				self.__search_filter.append(getattr(Users_table,key)==self.__args[key])

		if len(self.__search_filter) != 0:
			self.__data = self.__session.query(Users_table).filter(*self.__search_filter).order_by(Users_table.userid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

		else:
			self.__data = self.__session.query(Users_table).order_by(Users_table.userid).all()

			for d in self.__data:
				r = d.toJSONExcept()
				self._retval.append(r)

	def insert_user(self,**kwargs):

		user = Users_table()

		for key in kwargs:			
			if key in ('password'):
				try:
					setattr(user,key,self.encrypt_password(kwargs[key]))
				except TypeError:
					continue
			else:
				try:
					setattr(user,key,kwargs[key])
				except TypeError:
					continue


		self.__session.add(user)

		self.__session.commit()

		data = self.__session.query(Users_table).filter(Users_table.userid == user.userid)

		self._retval = list()

		for d in data:
			r = d.toJSONExcept()
			self._retval.append(r)

	def encrypt_password(self,password):
		converted_pass = str.encode(password)
		salt = bcrypt.gensalt()
		hashed = bcrypt.hashpw(converted_pass,salt)
		retval = hashed.decode('utf-8')

		return retval

	def __del__(self):
		if self.__session is not None:
			self.__session.close()

class Login_validation(object):
	def __init__(self,**kwargs):
		self.__session = Session()
		self.__data = ''
		self.__args = kwargs
		self.__search_filter = list()
		self.__search_param = ['username','password']
		self.__inputed_pass = None

		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,''):
				if key in ('username'):
					self.__search_filter.append(getattr(Users_table,key)==self.__args[key])
				elif key in ('password'):
					self.__inputed_pass = self.__args[key]

		if len(self.__search_filter) != 0:
			data = self.__session.query(Users_table).filter(*self.__search_filter)
			self.__data = [x for x in data]

	def validate(self):
		retval = dict()

		if len(self.__data) == 0:
			retval = {
				'status':'Failed',
				'data':[{'Message':'Invalid Credentials'}],
				'total':0
			}

			return retval

		username = getattr(self.__data[0],'username')
		hashed_password = str.encode(getattr(self.__data[0],'password'))
		inputed_pass = str.encode(self.__inputed_pass) if self.__inputed_pass is not None else str.encode('')

		if bcrypt.hashpw(inputed_pass,hashed_password) == hashed_password:
			retval = {
				'status':'OK',
				'data':[d.toJSONExcept() for d in self.__data],
				'total':1
			}

			http_session['username'] = username
		else:
			retval = {
				'status':'Failed',
				'data':[{'Message':'Incorrect Password'}],
				'total':0
			}

		return retval

	def __del__(self):
		if self.__session is not None:
			self.__session.close()
