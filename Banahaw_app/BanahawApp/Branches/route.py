from .controller import Branch

def add_route(api):
	api.add_resource(Branch, '/branch', endpoint='branch')