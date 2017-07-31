from .controller import Resevations

def add_route(api):
	api.add_resource(Resevations, '/reservations', endpoint='res')