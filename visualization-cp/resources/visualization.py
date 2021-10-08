import matplotlib.pyplot as plt
import io

def score_bar_plot(score):
    """Displays a barchart of the model scores"""
    f, ax = plt.subplots(figsize=(11, 9))
    plt.bar(score.keys(), score.values())
    plt.xlabel("Metric")
    plt.ylabel("Score")
    plt.title("Model scores")
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
