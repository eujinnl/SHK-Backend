from flask import Flask, jsonify

levels = [i for i in range(1, 11)] # 1 to 10 levels

def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello_world():
        return jsonify({"message": "Hello, World!"})
    
    @app.route("/")
    def hello():
        return jsonify({"message": "Hello, World!"})

    @app.route("/player-code/<levels>/submit",methods=['POST'])
    def handle_playercode(levels):
        if levels not in levels:
            return jsonify({"message": "Invalid level"}), 404

    return app