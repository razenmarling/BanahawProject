from .controller import Transactions

def add_route(api):
	api.add_resource(Transactions, '/transactions', endpoint='trans')