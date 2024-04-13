from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

import teams
import players
#import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

'''@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response'''

@app.route('/getTeam', methods=['GET'])
def get_teams():
    response = teams.get_all_teams(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertTeam', methods=['POST'])
def insert_team():
    request_payload = json.loads(request.form['data'])
    team_id = teams.insert_new_team(connection, request_payload)
    response = jsonify({
        'team_id': team_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllPlayer', methods=['GET'])
def get_all_orders():
    response = players.get_all_players(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertPlayer', methods=['POST'])
def insert_player():
    request_payload = json.loads(request.form['data'])
    player_id = players.insert_player(connection, request_payload)
    response = jsonify({
        'player': player_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteTeam', methods=['POST'])
def delete_product():
    return_id = teams.delete_product(connection, request.form['team_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)

