import pandas as pd # pyright: ignore[reportMissingModuleSource]
from sklearn.pipeline import Pipeline # pyright: ignore[reportMissingModuleSource]
from sklearn.feature_extraction.text import TfidfVectorizer # pyright: ignore[reportMissingModuleSource]
from sklearn.naive_bayes import MultinomialNB # pyright: ignore[reportMissingModuleSource]
from fetch_emails import get_messages
from auth_gmail import authenticate_gmail

# Load dataset
df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'text']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Train model
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])
model.fit(df['text'], df['label'])

# Fetch and classify emails
service = authenticate_gmail()
emails = get_messages(service)

for email in emails:
    prediction = model.predict([email])
    label = "Spam" if prediction[0] == 1 else "Not Spam"
    print(f"[{label}] {email}")
