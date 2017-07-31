from .controller import Member00

def add_route(api):
	api.add_resource(Member00, '/member00', endpoint="mem00")
	api.add_resource(Member00, '/member00/<char>', endpoint="mem00v")