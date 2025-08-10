new_email = ["Need 3 TikToks a day? Start here."]
X_new = vectorizer.transform(new_email) # pyright: ignore[reportUndefinedVariable]
prediction = model.predict(X_new) # pyright: ignore[reportUndefinedVariable]

if prediction[0] == 1:
    print("SPAM detected ✅")
else:
    print("Not Spam 🚫")
