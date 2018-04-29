from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
class MyDb():
    def __init__(self):
        self.client = MongoClient('localhost:27017')
        self.db=self.client.profiles
        self.serverStatusResult=self.db.command("serverStatus")
        
    def createDb():
        pass
    
@app.route("/")
def hello():
    obj=MyDb()
    return obj


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)

