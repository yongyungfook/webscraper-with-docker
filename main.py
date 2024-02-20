from flask import Flask
from flask import render_template
from scraper import scraper

app = Flask(__name__, template_folder='template')

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    data = scraper()
    url = "https://www.digiheritage.com/contact-us"
    return render_template("scraper.html", data=data, url=url)

if __name__ == "__main__":
    app.run(debug=True)