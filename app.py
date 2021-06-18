from flask import Flask, request
from flask_cors import CORS
from facebook_scraper import get_posts
import re

app = Flask(__name__)
CORS(app)

# RED SOCIAL DE FACEBOOK 

tag_regex_fecha = '([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?|GMT'

@app.route('/postFacebook') 
def users_Post():
    try:
#caracolradio, SaludEcuador, bbcnews, SaludEcuador, MinisterioDeGobiernoEcuador,lahoraecuador, elcomerciocom 
        
        return 'post'
    except:
        return 'No es un grupo publico de Facebook'

@app.route('/') 
def inicio():
    return "<h1> Api para Facebook</h1>"

if __name__ == "__main__":
    app.run()