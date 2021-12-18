from flask import Flask

from jsonrpc.backend.flask import api

app = Flask(__name__)
app.add_url_rule('/', 'api', api.as_view(), methods=['POST'])

@api.dispatcher.add_method
def my_method(*args, **kwargs):
    return args, kwargs
    
@api.dispatcher.add_method
def add(a, b):
    return a+b
    
    
if __name__=='__main__':
    app.run(debug=True)
