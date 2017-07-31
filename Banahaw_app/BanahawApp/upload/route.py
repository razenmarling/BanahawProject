from .controller import Uploadhandler

def add_route(api):
	api.add_resource(Uploadhandler, '/upload', endpoint='upload')
