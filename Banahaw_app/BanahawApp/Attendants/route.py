from .controller import Attendants

def add_route(api):
	api.add_resource(Attendants, '/attendants', endpoint='att')