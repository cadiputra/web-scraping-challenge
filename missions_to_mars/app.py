from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#import import_ipynb
import mission_to_mars


# Create an instance in Flasj
app = Flask (__name__)

# Establish connection using PyMongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html
@app.route("/")
def home():

    # Find one record from the database
    latest_news_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", news = latest_news_data)

# Route to trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    latest_news = mission_to_mars.scrape_info()

    # Update the Mongo database
    mongo.db.collection.update_one({},{"$set":latest_news}, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)



