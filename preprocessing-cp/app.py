from flask import Flask, json, request, Response, jsonify, send_file
import os
import pandas as pd
from resources import preprocess

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/preprocessing-cp/results', methods=['POST'])
def df_preprocessing():
    # db_api = os.environ['TRAININGDB_API']
    # content = request.get(db_api)
    content  = request.get_json()
    #df = pd.read_json(json.dumps(content), orient='records')
    #j = content.json()
    df = pd.DataFrame.from_dict(content)
    scaled_df = preprocess.preprocessing(df)
    return scaled_df

app.run(host='0.0.0.0', port=5000)