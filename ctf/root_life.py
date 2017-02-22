#!/usr/bin/python


import flask
import plyvel
from functools import wraps

'''
hacking 4 charities
goal of this is to create a realistic way of hacking in to a bank and takeing
over
'''

rl = flask.Flask(__name__) 

db = plyvel.DB('/tmp/db/l', create_if_missing=True)

def add_response_headers(headers={}):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			resp = flask.make_response(f(*args, **kwargs))
			h = resp.headers
			for header, value in headers.items():
				h[header] = value
			return resp
		return decorated_function
	return decorator


#stolen from layerprox
def antifingerprint(f):
	jibbrish = 'Bank Server'
	@wraps(f)	
	@add_response_headers({'Server': jibbrish})
	def decorated_function(*args, **kwargs):
		return f(*args, **kwargs)
	return decorated_function




#add header hack
#block robots

@rl.before_request
def blockuseragentreq():
	useragent = flask.request.headers['User-Agent']
	if 'sqlmap' in useragent:
		return flask.redirect(flask.url_for('dummy'))
	elif 'wget' in useragent:
		return flask.redirect(flask.url_for('dummy'))
	elif 'w3af' in useragent:
		return flask.redirect(flask.url_for('dummy'))
	elif 'curl' in useragent:
		return flask.redirect(flask.url_for('dummy'))
	elif 'Scanner' in useragent:
		return flask.redirect(flask.url_for('dummy'))        
	else:
		pass


@rl.route('/')
@antifingerprint
def index():
	return flask.render_template('index.html')

@rl.route('/login')
@antifingerprint
def login():
	return flask.render_template('login.html')

@rl.route('/join')
@antifingerprint
def join():
	if flask.request.method == 'POST':
		return ''' 
Invite only!
'''

	return flask.render_template('join.html')

@rl.route('/user/<user>')
@antifingerprint
def viewuser(user):
	balance = db.get(user) 

	return flask.render_template('user.html', balance=balance)

@rl.route('/home')
@antifingerprint
def user_home():
	return flask.render_template('home.html')

@rl.route('/robots.txt')
@antifingerprint
def robots():
	return ''' 
System administrator was here!, root it if u can

'''

@rl.route('/clueellerledtrad')
@antifingerprint
def clue():
	return ''' 

i like leveldb and it even got python bindings!

'''

@rl.route('/search/transaction/<keyword>', methods=['POST', 'GET'])
@antifingerprint
def searchtx(keyword):
	sn = db.snapshot()
	keyword = sn.get(keyword)
	return flask.render_template('search.html', keyword=keyword)	

@rl.route('/check/balance/<search>', methods=['GET'])
@antifingerprint
def checkbalance(search):
	s = db.get(search)
	return flask.render_template('check_balance', keyword=s)

@rl.route('/add/payment', methods=['POST', 'GET'])
@antifingerprint
def addpayment():
	if flask.request.method == 'POST':
		name = flask.request.form.get('name')
		money = flask.request.form.get('cash')
		name = name + '-'
		db.put(name, money)
		error = 'cash added!'
		return flask.render_template('add_payment.html', error=error)		

	return flask.render_template('add_payment.html')


if __name__  == '__main__':
	rl.run(debug=True, host='0.0.0.0',port=3389)
