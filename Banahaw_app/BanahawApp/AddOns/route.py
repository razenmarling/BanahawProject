from .controller import AddOns

def add_route(api):
	api.add_resource(AddOns,'/AddOns',endpoint='AO')