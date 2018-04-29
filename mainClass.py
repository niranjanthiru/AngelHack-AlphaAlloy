from flask import Flask, request, jsonify, url_for
from pymongo import MongoClient
import re

'''
self.client = MongoClient('localhost:27017')
self.db=self.client.profiles
self.serverStatusResult=self.db.command("serverStatus")
'''

class clientInterface:
    def __init__(self):
        self.app = Flask(__name__)
        self.client = MongoClient('localhost:27017')
    
        self.collection=self.client.Bar
        self.app.add_url_rule('/bars/<keyword>', None, self.bars, methods=['GET', 'POST','DELETE'])
        #self.app.add_url_rule('/stack/<name>', None, self.stack, methods=['GET', 'POST', 'DELETE'])
        #self.app.add_url_rule('/stack/<name>/output', None, self.stackOutput, methods=['GET'])
        #self.app.add_url_rule('/', None, self.siteMap, methods=['GET'])

    def post(self):
        self.collection.hotels.insert(
        [{
        "_id": 1,
        "name" : "Diff 42 Resto Lounge",
        "time-in" : "11AM",
        "time-out" : "12PM",
        "desc" : "Beer, cocktails & creative global eats in a relaxed space with dim lights & TVs tuned into sports.",
        "lat" : "12.975601",
        "long" : "80.221328",
        "image" :   "https://im1.dineout.co.in/images/uploads/restaurant/sharpen/9/l/f/p9581-147910157358294c85880c2.jpg"
        },
       {
        "_id": 2,
        "name" : "Glass Hopper",
        "time-in" : "1PM",
        "time-out" : "1AM",
        "desc" : "Grand lounge bar known for its world cigars and whiskeys at a high-end, palatial hotel",
        "lat" : "12.952926",
        "long" : "80.242255",
        "image" :   "https://im1.dineout.co.in/images/uploads/restaurant/sharpen/6/x/s/p6172-1432034551555b1cf7bf119.jpg"
        },

        {
        "_id": 3,
        "name" : "Hoppipola",
        "time-in" : "11AM",
        "time-out" : "12PM",
        "desc" : "Lounge and grill with contemporary artwork and lighting serving cocktails",
        "lat" : "13.044354",
        "long" : "80.263605",
        "image" :   "https://im1.dineout.co.in/images/uploads/restaurant/sharpen/1/y/g/p12532-149068160558d9ff05148ff.jpg"
        }]
        )

    def bars(self,keyword=None):
        """Print available apis."""
        #idvalue=int(request.view_args['UserId'])
        #print("idvalue type", type(idvalue))
        tmp=self.collection.hotels.find()
        tmp_list={}
        index=0
        for row in tmp:
            print("db vaue",row)
            tmp_list[index]=row
            index=index+1

        if request.method == 'GET':
            func_list = {"name" : "tamil"}
            return jsonify(tmp_list)
        if request.method == 'POST':
            findval=request.view_args['keyword']
            if findval != None :
                for row in tmp_list.values():
                    if re.search(findval,row['name'],re.IGNORECASE):
                        return jsonify(row)
                    else:
                        return jsonify({})
                        print(row)
            #return jsonify({"tamil" : "vanan"})
    def runApp(self):
        self.app.run(debug=True,host='0.0.0.0', port=9000)
    

if __name__ == "__main__":
    ci = clientInterface()
    #ci.post()
    ci.runApp()
