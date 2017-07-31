from .controller import Member01

def add_route(api):
	api.add_resource(Member01, "/member01", endpoint="mem01")
	api.add_resource(Member01, "/member01/<char>", endpoint="mem01v2")
