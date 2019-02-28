import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///YouTube_Top_Channels.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)


Channel = Base.classes.channel
# Use Pandas to perform the sql query
stmt = db.session.query(Channel).statement
df = pd.read_sql_query(stmt, db.session.bind)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/data")
def JSON_data():
    """Return JSONified data."""
    return df.to_json(orient = "records")


@app.route("/Channel/<channel>")
def channel_data(channel):
    """Return data for the specific channel."""

    ch = int(channel)
    channel_df = df.loc[df['id']== ch, :]
    return channel_df.to_json(orient = "records")



#Chris to try render channel.html with data populated
@app.route("/Channel_Chris/<channel>")
def channel_data(channel):
    """Return data for the specific channel."""

    ch = int(channel)    
    channel_df = df.loc[df['id']== ch, :]
    return channel_df.to_json(orient = "records")


if __name__ == "__main__":
    app.run()


