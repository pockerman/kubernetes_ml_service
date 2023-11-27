"""Driver code to train LogisticRegression classifier on
Iris dataset

"""

import pickle
from pathlib import Path
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


if __name__ == '__main__':

    # load the dataset
    iris = datasets.load_iris()

    print(f"Iris  DS keys {iris.keys()}")
    print(f"Iris features names {iris['feature_names']}")
    print(f"Iris target names {iris['target_names']}")

    data = iris['data']
    labels = iris['target']

    # we only take the first two features.
    X = data[:, :2]
    Y = labels

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42,
                                                        stratify=Y)

    # Create an instance of Logistic Regression Classifier and fit the data.
    logreg = LogisticRegression(C=1e5)
    logreg.fit(x_train, y_train)

    # save the model
    filename = Path('/home/alex/qi3/qi3_notes/projects/kubernetes_ingress_ml_service/serve_service/service/artifacts/iris_logreg_model.sav')
    pickle.dump(logreg, open(filename, 'wb'))

    print("=====================")
    print(x_test)
    print("=====================")
    print(y_test)
