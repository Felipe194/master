import Request 
from flask import Flask
from product import Product

app=Flask(__name__)


@app.route("/")
def hello_world():
    return "Hola"

@app.route("/search")
def search_product_in_wallapop():
    keywords="nintendo"
    wallapop_url=f"https://es.wallapop.com/app/search?keywords={bici}&filters_source=seo_landing"
    r=request.get(wallapop_url)
    
    return r.json()

if __name__ =="__main__":
    app.run(host="1270.0.0.1", port=5000)