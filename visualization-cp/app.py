from flask import Flask, json, request, Response, jsonify, send_file

from resources import visualization

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/visualization-cp/results', methods=['POST'])
def bar_plot():
    # receive the prediction request data as the message body
    content = request.get_json()
    scores = json.loads(content)
    bytes_object = visualization.score_bar_plot(scores)
    return send_file(bytes_object, attachment_filename = 'barchart.png', mimetype = 'image/npg')

app.run(host='0.0.0.0', port=5000)

# from flask import Flask, json, request, Response, jsonify
# import matplotlib.pyplot as plt
#
# from resources import visualization
#
# app = Flask(__name__)
# app.config["DEBUG"] = True
#
#
# @app.route('/visualization-cp/results', methods=['POST'])
# def bar_plot():
#     # receive the prediction request data as the message body
#     content = request.get_json()
#     scores = json.dumps(content)
#     plot = visualization.score_bar_plot(scores)
#     return plot
#
# app.run(host='0.0.0.0', port=5000)
