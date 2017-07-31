import os
from flask import Flask,render_template,send_file, make_response,send_from_directory
from flask import session, request
from flask_restful import Api

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__, static_url_path='')
api = Api(app)
app.secret_key = 'secret_key'
app.config.from_object('config')
http_session = session

# mysql+pymysql://{user}:{password}@{server}/{db}"
connstr = "mysql+pymysql://{user}:{password}@{server}/{db}".format(
	user=app.config['DB_USER'],
	password=app.config['DB_PASSWORD'],
	server=app.config['DB_SERVER'],
	db=app.config['DB_SCHEMA']
)

engine = create_engine(connstr, pool_size=20, max_overflow=100)

try:
	engine.connect()
	print('Connected')
except:
	print('Failed to Connect')

Session = sessionmaker(bind=engine)

# function for getting result
class Mini_func(object):

	def get_data(self):
		retval = dict()
		key = ['status','data','total']
		value = ['OK',self._retval,len(self._retval)]

		retval = dict(zip(key,value))

		return retval


@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin','*')
	response.headers.add('Access-Control-Allow-Headers','Content-type,Authorization')
	response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE')

	return response

@app.context_processor
def override_url_for():
	return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
	if endpoint == 'static':
		filename = values.get('filename', None)
		if filename:
			file_path = os.path.join(app.root_path,
				endpoint, filename)
			values['q'] = int(os.stat(file_path).st_mtime)
	return url_for(endpoint, **values)

# views
@app.route('/')
def index():
	try:
		http_session.pop('username',None)
	except:
		print('Error on Session')

	return render_template('banahaw.login.html')

@app.route('/admin')
def admin_page():
	#if 'username' in http_session:
        return render_template('admin.html')

	#return '<h1>Login Required<h1>'

@app.route('/user')
def user_page():
	if 'username' in http_session:
		return render_template('sample.html')

	return '<h1>Login Required<h1>'

@app.route("/download-reports/<filename>")
def download_file(filename=None):
	path = None
	if filename:
		print(filename)
		path = os.path.join(os.getcwd(), 'Reports', filename)

	return send_file(path, as_attachment=True)


import BanahawApp.Login
import BanahawApp.RegularServices
import BanahawApp.HealingPackage
import BanahawApp.AddOns
import BanahawApp.Branches
import BanahawApp.Attendants
import BanahawApp.Member00
import BanahawApp.Member01
import BanahawApp.Transaction
import BanahawApp.Reservations
import BanahawApp.Attendant01
import BanahawApp.Report
import BanahawApp.Product
import BanahawApp.Promo
import BanahawApp.FacialServices
import BanahawApp.upload

BanahawApp.Login.add_route(api)
BanahawApp.RegularServices.add_route(api)
BanahawApp.HealingPackage.add_route(api)
BanahawApp.AddOns.add_route(api)
BanahawApp.Branches.add_route(api)
BanahawApp.Attendants.add_route(api)
BanahawApp.Member00.add_route(api)
BanahawApp.Member01.add_route(api)
BanahawApp.Transaction.add_route(api)
BanahawApp.Reservations.add_route(api)
BanahawApp.Attendant01.add_route(api)
BanahawApp.Report.add_route(api)
BanahawApp.Product.add_route(api)
BanahawApp.Promo.add_route(api)
BanahawApp.FacialServices.add_route(api)
BanahawApp.upload.add_route(api)
