from flask_restful import Resource, reqparse
from .model import Reservations_data

class Resevations(Resource):
	def __init__(self):
		self.__reqparser = reqparse.RequestParser()
		self.__args = dict()

	def get(self):
		retval = dict()
		status = 200

		args_list = [('res_date',str,'json',None,False),
					 ('from',str,'args',None,False),
					 ('to',str,'args',None,False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		reservation = Reservations_data(**self.__args)
		reservation.get_reservations()
		result = reservation.get_data()
		retval = result

		return retval, status

	def post(self):
		status = 201

		args_list = [('transaction_type',str,'json',None,False),
					 ('client_name',str,'json',None,False),
					 ('member00id',int,'json',None,False),
					 ('client_type',str,'json',None,False),
					 ('branch',str,'json',None,False),
					 ('service_type',str,'json',None,False),
					 ('service',str,'json',None,False),
					 ('add_ons',str,'json',None,False),
					 ('products',str,'json',None,False),
					 ('attendant_name',str,'json',None,False),
					 ('attendantid',str,'json',None,False),
					 ('estimated_time',int,'json',None,False),
					 ('time_spent',int,'json',None,False),
					 ('total_amount',int,'json',None,False),
					 ('payment_type',str,'json',None,False),
					 ('service_price',int,'json',None,False),
					 ('add_ons_price',str,'json',None,False),
					 ('active',bool,'json',True,False),
					 ('datestart',str,'json',None,False),
					 ('dateend',str,'json',None,False),
					 ('res_date',str,'json',None,False),
					 ('res_time',str,'json',None,False)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		reservation = Reservations_data(**self.__args)

		reservation.post_reservations()

		return status

	def put(self):
		pass

	def delete(self):
		status = 204

		args_list = [('reservationid', int, 'args', 'None', True)]

		for args in args_list:
			self.__reqparser.add_argument(args[0],type=args[1],location=args[2],default=args[3],required=args[4])

		self.__args = self.__reqparser.parse_args()

		transaction = Reservations_data(**self.__args)
		transaction.get_reservations()
		result = transaction.del_reservations()

		return status