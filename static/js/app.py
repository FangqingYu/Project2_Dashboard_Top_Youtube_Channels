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

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Youtube_Top_Channels.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
# Channels_Metadata = Base.classes.channel_metadata
Channel = Base.classes.channel

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
#    """Return a list of sample names."""

#     Use Pandas to perform the sql query
   stmt = db.session.query(Samples).statement
   df = pd.read_sql_query(stmt, db.session.bind)

    Return a list of the column names (sample names)
   return jsonify(list(df.columns)[2:])


@app.route("/metadata/<channel>")
def sample_metadata(Channel):
    """Return the MetaData for a given channel."""
    sel = [
         Channel.name,
         Channel.Channel_Id,
         Channel.Channel_Description,
         Channel.Published_Date,
         Channel.Country,
         Channel.View_Count,
         Channel.Subscriber_Count,
         Channel.Video_Counts,
         Channel._Banner_Image,
    ]

    results = db.session.query(*sel).filter(Channel.channel == channel).all()
    #results = session.query(Channel).all()

    # Create a dictionary entry for each row of metadata information
    all_channels = []
for channel in results:
    channel_dict = {}
    channel_dict["Name"] = channel.Name
    channel_dict["Channel_Id"] = channel.Channel_Id
    channel_dict["Country"] = channel.Country
    all_channels.append(channel_dict)

    print(all_channels)
    return jsonify(all_channels)


@app.route("/Channels/<Channel_Name>")
def channels(channel):
    """Return `ids`, `Name`, `View_Count`, `Subscriber_Count`, `Video_Counts`, and `Channel_Id`."""
    stmt = db.session.query(Channel).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the channel id and
    # only keep rows with values above 1
    sample_data = df.loc[df[channel] > 1, ["Channel_Id", "Name", Channel]]
    # Format the data to send as json
    data = {
        "channel_id": sample_data.otu_id.values.tolist(),
        "sample_values": sample_data[sample].values.tolist(),
        "otu_labels": sample_data.otu_label.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
