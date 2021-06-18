from flask import Flask, request
from flask_cors import CORS
from facebook_scraper import get_posts
import re
import time
app = Flask(__name__)
CORS(app)

# RED SOCIAL DE FACEBOOK 

tag_regex_fecha = '([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?|GMT'

@app.route('/postFacebook') 
def users_Post():
    try:
#caracolradio, SaludEcuador, bbcnews, SaludEcuador, MinisterioDeGobiernoEcuador,lahoraecuador, elcomerciocom 
        group = request.args.get('group')
        time.sleep(2.4)
        posts = get_posts(group, pages=10)
        time.sleep(2.4)
        for post in posts:
            fecha = re.sub(tag_regex_fecha, '', str(post['time']))
            fechaG = re.sub('-', '/', fecha)
            users_locs = [{
                'descripcion': post['text'],
                'fecha': re.sub(r'(\d+)/(\d+)/(\d+)', r'\3/\2/\1', fechaG),
                'calificacion': '',
                'link':post['post_url'],
                'social':'Facebook',
                'noticia': post['text']
            } for post in  posts ]
            lista = users_locs
        return {'post': lista} 
    except:
        return 'No es un grupo publico de Facebook'

@app.route('/') 
def inicio():
    return "<h1> Api para Facebook</h1>"

if __name__ == "__main__":
    app.run()