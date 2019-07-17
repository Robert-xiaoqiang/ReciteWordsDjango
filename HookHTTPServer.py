import os
from wsgiref.simple_server import make_server
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	os.system('bash deploy.sh')

	return '<html><body><h1>I Knew!</h1></body></html>'

def main():
	httpd = make_server('', 8000, application)
	httpd.serve_forever()

if __name__ == '__main__':
	main()
