from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from champions import *

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<champ>')
def champ_page(champ):
    return render_template("champ.html")


class ChampionName(Resource):
    def get(self):
        return get_champ_by_name(request.args['name'])


class ChampionId(Resource):
    def get(self):
        return get_champ_by_id(request.args['id'])


class ChampionsContains(Resource):
    def get(self):
        return get_champs_containing(request.args['substring'])


class Champions(Resource):
    def get(self):
        return get_all_champs()


class ChampionsTrait(Resource):
    def get(self):
        args = request.args
        return get_champs_by_trait(args['trait'], args['value'])


api.add_resource(ChampionName, '/champion')
api.add_resource(ChampionId, '/championid')
api.add_resource(ChampionsContains, '/champion/contains')
api.add_resource(Champions, '/champions')
api.add_resource(ChampionsTrait, '/champions/trait')


if __name__ == '__main__':
    app.run()