from .controller import Login,LoginValidation

def add_route(api):
	api.add_resource(Login,'/login',endpoint='login')
	api.add_resource(LoginValidation,'/login/validation',endpoint='loginVal')