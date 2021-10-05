import matplotlib.pyplot as plt
import io

def score_bar_plot(score):
    f, ax = plt.subplots(figsize=(11, 9))
    plt.bar(score.keys(), score.values())
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

# import matplotlib.pyplot as plt
# from flask import jsonify
#
#
# def score_bar_plot(score):
#     # fig = plt.figure()
#     # ax = fig.add_axes([0,0,1,1])
#     # ax.bar(score.keys(), score.values())
#     #plt.show()
#     key = score.keys()
#     text_out = {
#         "Message:": "A plot was created :-)",
#         "Keys:": key
#     }
#     return jsonify(text_out), 200