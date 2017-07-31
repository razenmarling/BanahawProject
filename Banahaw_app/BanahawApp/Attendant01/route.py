from .controller import Attendants01

def add_route(api):
	api.add_resource(Attendants01, '/rawtime', endpoint='rawtime')