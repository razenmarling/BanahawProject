from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Facial_Services

class Facialmodel(Mini_func):
	def __init__(self, **kwargs):
		self.__session = Session()
		self.__args = kwargs

	def get_services(self):
		retval = None

		result = self.__session.query(T_Facial_Services).all()

		temp_list = list()
		for d in result:
			r = d.toJSONExcept()
			temp_list.append(r)

		if temp_list:
			retval = temp_list

		return retval

	def insert_facial_service(self, **kwargs):
		fservices = T_Facial_Services()

		for key, value in kwargs.items():
			try:
				setattr(fservices,key,value)
			except TypeError:
				continue

		self.__session.add(fservices)

		self.__session.commit()

	def del_facial_service(self, **kwargs):
		fsid = kwargs.get('id', 0)

		resdata = self.__session.query(T_Facial_Services).filter(T_Facial_Services.facial_services_id == fsid).first()

		if resdata:
			self.__session.delete(resdata)

		try:
			self.__session.commit()
		except:
			self.__session.rollback()

	def edit_facial_services(self, **kwargs):
		facialid = kwargs.get('facial_services_id', 0)

		result = self.__session.query(T_Facial_Services).filter(T_Facial_Services.facial_services_id==facialid).first()

		update_param = ['member_price', 'non_member_price', 'duration']

		for param in update_param:
			data = kwargs.get(param, None)

			if data:
				try:
					setattr(result, param, data)
				except TypeError:
					continue

		self.__session.commit()

