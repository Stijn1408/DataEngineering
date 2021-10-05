import matplotlib.pyplot as plt

def score_bar_plot(score):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(score.keys(), score.values())
    plt.show()
