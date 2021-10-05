from flask import Flask, json, request, Response, jsonify
import matplotlib.pyplot as plt

from resources import visualization

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/visualization-cp/results', methods=['POST'])
def bar_plot():
    # receive the prediction request data as the message body
    content = request.get_json()
    scores = json.loads(content)
    visualization.score_bar_plot(scores)

app.run(host='0.0.0.0', port=5000)
