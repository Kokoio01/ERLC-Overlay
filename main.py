from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import requests
import os

load_dotenv()
app = Flask(__name__)

API_URL = "https://api.policeroleplay.community/v1/server"
API_KEY = os.getenv('API_KEY')

@app.route('/')
def index():
    return render_template('erlc.html')

@app.route('/api/server-data', methods=['GET'])
def get_server_data():
    try:
        headers = {
            'server-key': API_KEY
        }
        
        response = requests.get(API_URL, headers=headers)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch data from API"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/player-data', methods=['GET'])
def get_player_data():
    try:
        headers = {
            'server-key': API_KEY
        }
        
        player_api_url = f"{API_URL}/players"
        response = requests.get(player_api_url, headers=headers)
        
        if response.status_code == 200:
            player_data = response.json()
            team_counts = {'Civilian': 0, 'Police': 0, 'Sheriff': 0, 'Fire': 0, 'DOT': 0}
            total_players = 0
            
            for player in player_data:
                team = player.get('Team', 'Unknown')
                if team in team_counts:
                    team_counts[team] += 1
                total_players += 1
            
            team_counts['TotalPlayers'] = total_players
            
            return jsonify(team_counts)
        else:
            return jsonify({"error": "Failed to fetch player data from API"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
