
from flask import Flask

app = Flask('ping')

@app.route('/ping', methods=['GET']) # this is a decorator for added functionality
def ping():
    return 'PONG'

# has to be saved in the directory where you are going to do the import
# in terminal:
# ipython
# import ping
# ping.ping()

if __name__ == "__main__": # python main method
    app.run(debug=True, host='0.0.0.0', port=9696) # host is the same as writing localhost

#try the service from:
# the terminal using curl http://0.0.0.0:9696/ping
# or from a browser http://localhost:9696/ping