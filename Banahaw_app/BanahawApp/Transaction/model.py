import datetime
from sqlalchemy import and_,desc
from BanahawApp import Session,Mini_func
from BanahawApp.table import T_Transaction


class Transactions_data(Mini_func):
	def __init__(self,querytype='all',**kwargs):
		self.__session = Session()
		self.__args = kwargs
		self._retval = list()
		self.__search_filter = list()
		self.__search_param = ['active','transaction_type','transactionid','attendantid', 'member00id']
		self.__data = None

		for key in self.__search_param:
			if key in self.__args and self.__args[key] not in (None,""):
				self.__search_filter.append(getattr(T_Transaction,key) == self.__args[key])

		ds = self.__args.get('from',None)
		de = self.__args.get('to',None)

		if ds and de:
			self.__search_filter.append(getattr(T_Transaction,'datecreated').between(ds,de))

		if self.__search_filter:
			self.__data = self.__session.query(T_Transaction).filter(
				and_(*self.__search_filter)).order_by(T_Transaction.datestart).all()

			for d in self.__data:
				r = d.toJSONExcept()
				time = datetime.datetime.strptime(r['datestart'],'%m/%d/%Y %H:%M')
				r['started'] = time.time().strftime("%I:%M %p")
				etime = time + datetime.timedelta(minutes=int(d.estimated_time))
				r['endtime'] = etime.strftime("%I:%M %p")
				self._retval.append(r)

		elif querytype is not None:
			self.__data = self.__session.query(T_Transaction).order_by(T_Transaction.datestart).all()

			for d in self.__data:
				r = d.toJSONExcept()
				time = datetime.datetime.strptime(r['datestart'],'%m/%d/%Y %H:%M')
				r['started'] = time.time().strftime("%I:%M %p")
				etime = time + datetime.timedelta(minutes=int(d.estimated_time))
				r['endtime'] = etime.strftime("%I:%M %p")
				self._retval.append(r)

	def insert_transaction(self,**kwargs):

		transaction = T_Transaction()

		for key in kwargs:
			try:
				setattr(transaction,key,kwargs[key])
			except TypeError:
				continue

		self.__session.add(transaction)

		self.__session.commit()

	def edit_transaction(self,**kwargs):
		update_kwargs = kwargs
		search_param = ['transactionid']
		search_filter = list()

		for key in search_param:
			if key in update_kwargs and update_kwargs[key] not in (None,''):
				search_filter.append(getattr(T_Transaction,key)==update_kwargs[key])

		if search_filter:
			retval = True
			self.__data = self.__session.query(T_Transaction).filter(
				and_(*search_filter)).order_by(T_Transaction.datestart).all()
		else:
			retval = False

		update_list = ['payment_type', 'dateend', 'time_spent', 'active', 'service_type'
					   ,'service', 'add_ons', 'attendant_name', 'attendantid', 'estimated_time', 
					   'total_amount', 'service_price', 'add_ons_price']

		for obj in self.__data:
			for key in update_list:
				if key in update_kwargs and update_kwargs[key] is not None:
					if key == 'dateend':
						update_kwargs[key] = datetime.datetime.strptime(update_kwargs[key], '%m/%d/%Y, %I:%M:%S %p')
					try:
						setattr(obj,key,update_kwargs[key])
					except TypeError:
						continue

		self.__session.commit()

		return retval

	def del_transaction(self):
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
		

	def __del__(self):
		self.__session.close()