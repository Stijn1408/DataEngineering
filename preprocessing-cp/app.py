from flask import Flask, json, request, Response, jsonify, send_file

from resources import preproces

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/preprocessing-cp/results', methods=['POST'])
def df_preprocessing():
    content = request.get_json()
    df = pd.read_json(json.dumps(content), orient='records')
    scaled_df = preproces.preprocessing(df)
    return scaled_df

app.run(host='0.0.0.0', port=5000)