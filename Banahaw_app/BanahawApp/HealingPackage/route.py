from .controller import HealingPackages

def add_route(api):
	api.add_resource(HealingPackages,'/HealingPackages',endpoint='HP')