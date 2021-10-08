from flask import Flask, json, request, Response, jsonify, send_file

from resources import sampleprediction
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/sample-cp/results', methods=['POST'])
def sample_plot():
    """Displays a html table of a random sample of all predictions"""
    content = request.get_json()
    df = pd.read_json(json.dumps(content), orient='records')
    table = sampleprediction.sample_plot(df)
    return table.to_html(header = True, table_id = "Random Prediction Sample")

app.run(host='0.0.0.0', port=5000)


