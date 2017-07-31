from .controller import Promohandler

def add_route(api):
	api.add_resource(Promohandler, "/promos")
