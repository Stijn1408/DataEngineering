import matplotlib.pyplot as plt
import io

def score_bar_plot(score):
    f, ax = plt.subplots(figsize=(11, 9))
    plt.bar(score.keys(), score.values())
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
