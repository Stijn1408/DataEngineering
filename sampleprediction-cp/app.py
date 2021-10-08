from flask import Flask, json, request, Response, jsonify, send_file

from resources import sampleprediction
import ast
import requests
import pandas as pd
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/sample-cp/results', methods=['POST'])
def sample_plot():
    # receive the prediction request data as the message body
    db_api = os.environ['PREDICTION_API']
    content = requests.get(db_api)
    content = content.json()
    df = pd.read_json(json.dumps(content), orient='records')
    table = sampleprediction.sample_plot(df)
    return table.to_html(header = True, table_id = "Random Prediction Sample")

app.run(host='0.0.0.0', port=5000)


