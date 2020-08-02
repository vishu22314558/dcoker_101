from flask import Flask

server = Flask(__name__)

@server.route("/")
@server.route("/home")
def home():
    return "Hello Docker"

if __name__ =="__main__":
    server.run(debug=True , host='0.0.0.0')

#Using host=0.0.0.0 let you access your app through your local network.