from .controller import Producthandler

def add_route(api):
	api.add_resource(Producthandler, "/products", endpoint="prod")