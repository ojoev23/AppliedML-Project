import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Get engineered data
df = pd.read_csv("../data/AAPL_engineered.csv")

# Separate X to encoded columns and y to target column
X = df[['Day_Monday', 'Day_Tuesday', 'Day_Wednesday', 'Day_Thursday', 'Day_Friday', 'RSI_Scaled']]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=50)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy score: ", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
plt.barh(model.feature_names_in_, model.feature_importances_)
plt.show()