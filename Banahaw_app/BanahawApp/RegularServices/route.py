from .controller import RegularServices

def add_route(api):
	api.add_resource(RegularServices,'/RegularServices',endpoint='RS')