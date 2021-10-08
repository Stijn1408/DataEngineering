from flask import Flask, json, request, Response, jsonify, send_file

from resources import visualization
import ast

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/visualization-cp/results', methods=['POST'])
def bar_plot():
    """Create a barchart and display this as npg"""
    content = request.get_json()
    scores = json.dumps(content)
    scores = ast.literal_eval(scores)
    bytes_object = visualization.score_bar_plot(scores)
    return send_file(bytes_object, attachment_filename = 'barchart.png', mimetype = 'image/npg')

app.run(host='0.0.0.0', port=5000)
