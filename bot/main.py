import re

def analyze_text(text):
    spam_keywords = [
        "win", "free", "urgent", "money", "credit", "loan", "offer", "click here",
        "limited time", "100% free", "act now", "don't miss", "lottery", "congratulations"
    ]
    
    text = text.lower()
    score = 0
    matched = []

    for keyword in spam_keywords:
        if re.search(rf"\b{keyword}\b", text):
            matched.append(keyword)
            score += 10

    score = min(score, 100)  # Max cap

    if score > 50:
        result = f"🚨 Likely spam. Detected: {', '.join(matched)}"
    elif score > 20:
        result = f"⚠️ Possibly spam. Words matched: {', '.join(matched)}"
    else:
        result = "✅ Message looks safe."

    return {"result": result, "score": score}
