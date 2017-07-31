from .controller import Reporthandler, Reporthandler2, Reporthandler3

def add_route(api):
	api.add_resource(Reporthandler, "/report-attendants", endpoint="attreport")
	api.add_resource(Reporthandler2, "/report-summary", endpoint="attsum")
	api.add_resource(Reporthandler3, "/members-list", endpoint="memlist")
	