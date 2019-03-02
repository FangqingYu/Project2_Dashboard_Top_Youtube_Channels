
App Description: <hr>

We used the Kaggle YouTube datasets to identify the top 100 YouTube channels and then used the YouTube API to retrieve the information for these channels. The retrieved information was loaded to a SQLite database and a CSV file. The database is used by the Flask app to render the HTML pages and the CSV file is used by Tableau to generate the visualizations.



<hr>

Contents of the Git Repo:<hr>


data:
-----
    1) Top83_YouTube_Channels.csv: Channel information extracted using YouTube Data API.
    2) kaggle_data.csv: Used this dataset to shortlist the top 100 youtube channels based on their rank.


db:
-------
database folder 
    1) YouTube_Top_Channels.sqlite <Strong> move to db folder? </strong> sqlite database containing the top 83 youtube channels retrieved with the YouTube API.

static: 
-------
contains the css and js components
    a) css folder:
        1) bootstrap.min.css: Bootstrap css
        2) style.css: local css

    b) js folder: 
        1) logic.js: javascript to add interactivity to pages.


templates: 
----------
contains the HTML components
    1) challenges.html
    2) channel.html
    3) data.html
    4) index.html: landing page
    5) money.html
    6) Subscribers.html
    7) visualization_1.html
    8) visualization_2.html
    9) visualization_3.html
    10) Who.html


Flask app:
-----------
app.py


Tableau visualizations:
------------------------
youtube_book.twb 







Jupyter Notebooks:
---------------------
<strong>Francis to decide which one(s) to keep:</strong>
    1) YouTube_ad_API exploration.ipynb
    2) YouTube_API_exploration.ipynb
    3) YouTube_Data_Integration.ipynb

random folder:
    1) Trending_Videos_WebScraping:




