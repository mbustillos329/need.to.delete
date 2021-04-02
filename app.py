from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# create flask app
app = Flask(__name__)

# # set up mongo connection 
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# # Create connection variable


# # Pass connection to the pymongo instance.
client = PyMongo.MongoClient('mongodb://localhost:27017')
mydb = myclient["mars_db"]

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Connect to a database. Will create one if not already available.
db = client.mars_db

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

