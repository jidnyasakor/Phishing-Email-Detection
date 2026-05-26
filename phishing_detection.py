import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("emails.csv")

# Function to extract URL count
def extract_features(text):
    urls = re.findall(r'http[s]?://\S+', text)
    return len(urls)

# Add URL feature
data['url_count'] = data['text'].apply(extract_features)

X = data['text']
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(
        stop_words='english'
    )),
    ('classifier', MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test,predictions)

print("\nModel Accuracy:",accuracy*100,"%")

# Confusion Matrix
cm = confusion_matrix(y_test,predictions)

print("\nConfusion Matrix:")
print(cm)

# Plot
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    xticklabels=['Phishing','Safe'],
    yticklabels=['Phishing','Safe']
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# User testing
while True:

    mail=input("\nEnter email text: ")

    result=model.predict([mail])

    if result[0]=="phishing":
        print("⚠ Phishing Email Detected")
    else:
        print("✓ Safe Email")

    choice=input("Check another? y/n:")

    if choice=="n":
        break