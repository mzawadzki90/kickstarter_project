import matplotlib.pyplot as plt

from keras.callbacks import History


class LossPlotter:
    history: History

    def __init__(self, history):
        self.history = history

    def plot(self):
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')
        plt.show()
