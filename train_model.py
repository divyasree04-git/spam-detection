# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample dataset (you can replace this with a larger dataset or CSV)
data = {
    'text': [
        "Congratulations! You've won a $1000 gift card. Click here to claim now!",
        "Get cheap meds without prescription. Limited offer!!!",
        "Earn money from home in 3 easy steps. No experience needed!",
        "Your Amazon order has been shipped and will arrive soon.",
        "Update your account info to avoid suspension.",
        "Happy Birthday! Wishing you a wonderful day."
    ],
    'label': [1, 0, 1, 0, 1, 0]  # 1 = SPAM, 0 = NOT SPAM
}

df = pd.DataFrame(data)

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])

# Train model
pipeline.fit(df['text'], df['label'])

# Save model and vectorizer
joblib.dump(pipeline, 'spam_model.pkl')
print("✅ Model trained and saved as 'spam_model.pkl'")
