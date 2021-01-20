"""
Our goal in this section is to plot our 300 dimensions vectors into 2 dimensional graphs, and see if we can spot
interesting patterns.
For that we are going to use t-SNE implementation from scikit-learn.
To make the visualizations more relevant, we will look at the relationships between a query word (in red),
its most similar words in the model (in blue), and other words from the vocabulary (in green).

t-SNE visualizations:
t-SNE is a non-linear dimensionality reduction algorithm that attempts to represent high-dimensional data and the
underlying relationships between vectors in a lower-dimensional space.
Here is a good tutorial on it: https://medium.com/@luckylwk/visualising-high-dimensional-datasets-using-pca-and-t-sne-in-python-8ef87e7915b
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


class TSNEScatterPlotter:
    wv: Word2Vec

    def __init__(self, wv):
        self.wv = wv
        sns.set_style("darkgrid")

    def plot(self, word, list_names):
        """ Plot in seaborn the results from the t-SNE dimensionality reduction algorithm of the vectors of a query word,
        its list of most similar words, and a list of words.
        """
        arrays = np.empty((0, 300), dtype='f')
        word_labels = [word]
        color_list = ['red']

        # adds the vector of the query word
        arrays = np.append(arrays, self.wv.__getitem__([word]), axis=0)

        # gets list of most similar words
        close_words = self.wv.most_similar([word])

        # adds the vector for each of the closest words to the array
        for wrd_score in close_words:
            wrd_vector = self.wv.__getitem__([wrd_score[0]])
            word_labels.append(wrd_score[0])
            color_list.append('blue')
            arrays = np.append(arrays, wrd_vector, axis=0)

        # adds the vector for each of the words from list_names to the array
        for wrd in list_names:
            wrd_vector = self.wv.__getitem__([wrd])
            word_labels.append(wrd)
            color_list.append('green')
            arrays = np.append(arrays, wrd_vector, axis=0)

        # Reduces the dimensionality from 300 to 50 dimensions with PCA
        reduc = PCA(n_components=19).fit_transform(arrays)

        # Finds t-SNE coordinates for 2 dimensions
        np.set_printoptions(suppress=True)

        Y = TSNE(n_components=2, random_state=0, perplexity=15).fit_transform(reduc)

        # Sets everything up to plot
        df = pd.DataFrame({'x': [x for x in Y[:, 0]],
                           'y': [y for y in Y[:, 1]],
                           'words': word_labels,
                           'color': color_list})

        fig, _ = plt.subplots()
        fig.set_size_inches(9, 9)

        # Basic plot
        p1 = sns.regplot(data=df,
                         x="x",
                         y="y",
                         fit_reg=False,
                         marker="o",
                         scatter_kws={'s': 40,
                                      'facecolors': df['color']
                                      }
                         )

        # Adds annotations one by one with a loop
        for line in range(0, df.shape[0]):
            p1.text(df["x"][line],
                    df['y'][line],
                    '  ' + df["words"][line].title(),
                    horizontalalignment='left',
                    verticalalignment='bottom', size='medium',
                    color=df['color'][line],
                    weight='normal'
                    ).set_size(15)

        plt.xlim(Y[:, 0].min() - 50, Y[:, 0].max() + 50)
        plt.ylim(Y[:, 1].min() - 50, Y[:, 1].max() + 50)

        plt.title('t-SNE visualization for {}'.format(word.title()))
