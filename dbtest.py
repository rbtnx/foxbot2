from sqlalchemy import *
from sqlalchemy.dialects import postgresql
from website.dbmodel import db, Game
from website.views.site import map_mechanic
from startup import app

# database = create_engine('postgresql://kathrin:password@localhost:5433/gamepicker')
# metadata = MetaData(database)

# gamesTab = Table('games', metadata,
#     Column('gid', Integer, primary_key=True),
#     Column('name', String(40)),
#     Column('max_player', Integer),
#     Column('best_playnum', postgresql.ARRAY(Integer))
# )
# gamesTab.create()

# i = gamesTab.insert()
# i.execute(name='Marco Polo', max_player=30, best_playnum=[3, 4, 5])
# i.execute({'name': 'John', 'max_player': 42},
#           {'name': 'Susan', 'max_player': 57},
#           {'name': 'Carl', 'max_player': 33})

# find stuff in array:
# game = Game.query.filter(5 == Game.best_playnum.any_()).first() 

def process():
    app.app_context().push()
    db.init_app(app) 
    playnum = 4
    playtime = 90
    weight = 0
    mechanics = ['tilePlace']
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

    return games