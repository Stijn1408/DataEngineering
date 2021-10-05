import matplotlib.pyplot as plt
from flask import jsonify


def score_bar_plot(score):
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    # ax.bar(score.keys(), score.values())
    #plt.show()
    key = score.keys()
    text_out = {
        "Message:": "A plot was created :-)",
        "Keys:": key
    }
    return jsonify(text_out), 200