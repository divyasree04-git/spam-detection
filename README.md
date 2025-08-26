# 📧 Spam Detection using Machine Learning

This project is a **Spam Email Detection System** built with **Python, Scikit-learn, and Natural Language Processing (NLP)**.
It classifies incoming emails as **Spam** or **Not Spam (Ham)** and also integrates with the **Gmail API** for real-time analysis.

## 🚀 Features

* 📊 **Text Preprocessing** using TF-IDF vectorization
* 🤖 **Machine Learning Model** (Naive Bayes Classifier) for spam detection
* 📬 **Gmail API Integration** to fetch and classify real emails
* 🖥 **Flask Web Application** interface for testing emails
* 💾 Save/Load trained models for reuse

## 🛠 Tech Stack

* Python 3.9+
* Scikit-learn
* Numpy & Pandas
* Flask
* Gmail API (Google OAuth 2.0)

## 📂 Project Structure

```bash
spam-detection/
├── app.py                  # Flask web app
├── spam_detector.py        # ML Model training & prediction
├── auth_gmail.py           # Gmail API authentication
├── templates/              # HTML templates for Flask
│   └── index.html
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── dataset/                # (Optional) Training dataset


## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/divyasree04-git/spam-detection.git
cd spam-detection
```

2. **Create a virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 Gmail API Setup (Optional)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project → Enable **Gmail API**
3. Configure **OAuth 2.0 credentials** → Download `credentials.json`
4. Place `credentials.json` in the project root directory

---

## ▶️ Run the App

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000/`
https://znb9lskw-5000.inc1.devtunnels.ms/

---

## 🧪 Example Usage

* Enter a sample email text in the web app to test spam detection
* Fetch real emails from your Gmail inbox (if Gmail API is configured)
* View the prediction:

  * ✅ Ham → Safe email
  * 🚫 Spam → Detected as spam

---

## 📸 Demo Screenshot
<img width="1783" height="872" alt="Screenshot 2025-08-26 223607" src="https://github.com/user-attachments/assets/ef744e51-8efa-4ec2-a27e-316e3b1c5dd5" />

<img width="1849" height="880" alt="image" src="https://github.com/user-attachments/assets/49402557-3dda-4b49-9228-27260e3e17d1" />


## 📌 Future Improvements

* Improve accuracy with deep learning models
* Add visualization dashboard
* Deploy to **Heroku / Streamlit Cloud**


## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.
