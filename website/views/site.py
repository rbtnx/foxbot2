from flask import Blueprint, render_template, request
from sqlalchemy import or_
from website.dbmodel import Game

site = Blueprint('site', __name__, template_folder="../templates")

def map_mechanic(arg):
    mapper = {
        'coop': 'Co-operative Play',
        'cardDraft': 'Card Drafting',
        'tilePlace': 'Tile Placement',
        'areaControl': 'Area Control / Area Influence',
        'deckBuild': 'Deck / Pool Building',
        'workerPlace': 'Worker Placement',
    }
    return mapper.get(arg, None)

@site.route('/', methods=['GET', 'POST'])
def index():
    numgames = Game.query.count()
    return render_template('index.html', numgames=numgames)

@site.route('/process', methods=['GET', 'POST'])
def process():
    playnum = request.form['playnum']
    playtime = request.form['playtime']
    weight = int(request.form['rating'])
    mechanics = request.form.getlist('mechCheck')
    if (playnum and playtime):
        gamequery = Game.query.filter(Game.maxplayers >= playnum, playnum == Game.best_playnum.any_(),
                                        Game.max_playing_time <= playtime)
        if weight:
            clamp = lambda n: max(min(5, n), 0)
            min_weight = clamp(weight - 0.5)
            max_weight = clamp(weight + 0.5)
            gamequery = gamequery.filter(Game.average_weight.between(min_weight, max_weight))

        mlist = []
        for m in mechanics:
            mlist.append(map_mechanic(m))
        
        if mlist:
            gamequery = gamequery.filter(or_(Game.mechanics.any_() == m for m in mlist))
        
        gamequery = gamequery.order_by(Game.bgg_rank)
        games = gamequery.all()

        return render_template('showgames.html', games=games, n=range(len(games)))
    return("Ooops.. you didn't fill out all the questions..")
