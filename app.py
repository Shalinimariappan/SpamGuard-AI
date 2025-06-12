from flask import Flask, render_template, request, send_file
from fpdf import FPDF
from googletrans import Translator
import os
import random

app = Flask(__name__)
translator = Translator()

SPAM_KEYWORDS = {
    'lottery': ['won', 'prize', 'congratulations', 'lakh'],
    'job scam': ['work from home', 'job offer', 'salary', 'interview'],
    'phishing': ['OTP', 'account', 'verify', 'login'],
}

REPLIES = {
    'lottery': "I'm not interested. Please do not contact me again.",
    'job scam': "I will report this to authorities if contacted again.",
    'phishing': "This message looks suspicious. I'm securing my accounts.",
}

def classify_spam(text):
    scores = {k: 0 for k in SPAM_KEYWORDS}
    for category, keywords in SPAM_KEYWORDS.items():
        for word in keywords:
            if word.lower() in text.lower():
                scores[category] += 1
    spam_type = max(scores, key=scores.get)
    return spam_type if scores[spam_type] > 0 else 'unknown'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form.get("user_input", "")
        lang_detected = translator.detect(text).lang
        translated_text = translator.translate(text, dest='en').text if lang_detected != 'en' else text

        spam_type = classify_spam(translated_text)
        is_spam = spam_type != 'unknown'
        score = random.randint(70, 99) if is_spam else random.randint(0, 40)

        result = {
            'original_text': text,
            'translated': translated_text,
            'lang': lang_detected,
            'type': spam_type,
            'score': score,
            'reply': REPLIES.get(spam_type, "No response needed."),
        }
    return render_template('index.html', result=result)

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    content = request.form.get('pdf_content')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)
    file_path = "spam_report.pdf"
    pdf.output(file_path)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
