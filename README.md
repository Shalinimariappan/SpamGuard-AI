# 🚨 SpamGuard AI

SpamGuard AI is a smart and secure web application that uses artificial intelligence to detect spam, scam, and fraudulent messages. Whether it's a suspicious WhatsApp forward, email message, or social media text — SpamGuard AI helps users analyze, understand, and respond to digital threats effectively.

---

## 🔍 Features

- ✅ **Spam Detection:** Classifies text as spam or not using an AI/ML model.
- 🎯 **Spam Risk Scoring:** Shows likelihood of the message being spam using a visual progress bar.
- 🎤 **Voice-to-Text Input:** Convert speech into text for scam detection (ideal for voice messages).
- 🌗 **Light/Dark Mode Toggle:** Switch between dark and light UI themes.
- 🌐 **Multilingual Input:** Supports input in multiple languages using translation before classification.
- 💬 **Smart Reply Suggestions:** Gives AI-suggested safe responses to scam messages.
- 📄 **PDF Export:** Export detailed analysis as a PDF using `fpdf` or `pdfkit`.
- 🧠 **Daily Tips:** Educates users with tips to avoid common scams and phishing tactics.

---

## 🛠 Tech Stack

| Layer           | Technology                      |
|----------------|----------------------------------|
| Frontend        | HTML, Tailwind CSS, JavaScript   |
| Backend         | Python (Flask)                   |
| ML Model        | Scikit-learn (Naive Bayes)       |
| Voice Input     | Web Speech API / `speech_recognition` |
| PDF Export      | `fpdf` / `pdfkit`                |
| Translation     | `googletrans` or similar         |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.10+ installed and Git.

### Installation

```bash
git clone https://github.com/Shalinimariappan/SpamGuard-AI.git
cd SpamGuard-AI
pip install -r requirements.txt
python app.py
