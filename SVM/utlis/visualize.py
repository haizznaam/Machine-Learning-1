import numpy as np
import matplotlib.pyplot as plt




def plot_data(X, y):
    """
    Plots the data points X and y into a new figure.

    Parameters
    ----------
    X : ndarray, shape (n_samples, n_features)
        Training vectors, where n_samples is the number of samples and n_features is the number of features.
    y : ndarray, shape (n_samples,)
        Target values (class labels in classification).
    """

    neg = np.where(y == 0)[0]
    pos = np.where(y == 1)[0]

    plt.scatter(X.iloc[neg, 0], X.iloc[neg, 1], marker='o',
                label='negative', color='midnightblue')
    plt.scatter(X.iloc[pos, 0], X.iloc[pos, 1],
                marker='+', label='positive', color='y')

    plt.legend()



def visualize_boundary(X, y, clf):
    """
    Plots a linear decision boundary learned by the SVM.

    Parameters
    ----------
    X : ndarray, shape (n_samples, n_features)
        Samples, where n_samples is the number of samples and n_features is the number of features.
    y : ndarray, shape (n_samples,)
        Labels.
    clf : sklearn.svm.classes.SVC
        The trained SVM.
    """

    plot_data(X, y)
    
    x1_plot = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100)
    x2_plot = np.linspace(np.min(X[:, 1]), np.max(X[:, 1]), 100)
    X1, X2 = np.meshgrid(x1_plot, x2_plot)
    vals = np.zeros(X1.shape)

    for i in range(X1.shape[1]):
        X_tmp = np.hstack((X1[:, i:i + 1], X2[:, i:i + 1]))
        vals[:, i] = clf.predict(X_tmp)
    plt.contour(X1, X2, vals, levels=[0])
