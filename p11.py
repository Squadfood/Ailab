from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets

# Load the dataset
iris = datasets.load_iris()
x = iris.data
y = iris.target

# Print features and labels
print("Features: ", iris.feature_names)
print(x)
print("Labels: ", iris.target_names)
print(y)

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y)

# Train the K-Nearest Neighbors classifier
classifier = KNeighborsClassifier()
classifier.fit(x_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(x_test)

# Print the confusion matrix and classification report
print('Confusion Matrix')
print(confusion_matrix(y_test, y_pred))
print('Accuracy Metrics')
print(classification_report(y_test, y_pred))
