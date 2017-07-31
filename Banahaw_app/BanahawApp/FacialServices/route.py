from .controller import Facialhandler

def add_route(api):
	api.add_resource(Facialhandler, '/facialservices')