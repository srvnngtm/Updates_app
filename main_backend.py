""" imports"""

from flask import Flask , render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo

"""initializing database connection and mongodb app"""

app =Flask(__name__)

app.config['MONGO_DBNAME'] = 'updates_app'
app.config['MONGO_URI']= 'mongodb://saravanan:saravanan1@ds117535.mlab.com:17535/updates_app'

mongo = PyMongo(app)

"""
data migration from main table to respective circles depending on the visibility of that data
"""
@app.route('/add')
def add():
    data=mongo.db.main
    
    datastr=""
    num_of_entries = data.find({}).count()
    for i in range(num_of_entries):
        buffer = data.find_one({})
        data.delete_one({})
        datastr+=buffer['data']
        datastr+='        '
        if int(buffer['circle'])==1:
            insert_db=mongo.db.circle1
            insert_db.insert({"data":buffer['data']})
        elif  int(buffer['circle'])==2:
            insert_db=mongo.db.circle2
            insert_db.insert({"data":buffer['data']})
        
    return 'the data is '+datastr



if __name__ =='__main__':
    app.run(debug=True)