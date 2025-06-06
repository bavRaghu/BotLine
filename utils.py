import re
import json
from rapidfuzz import fuzz

def readFAQS(path="faqs.json"):
    with open(path, "r") as file:
        return json.load(file)

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower().strip())

def matchScore(user_ip, faqs):

    user_ip_clean = clean_text(user_ip)
    max_score = 0
    best_qs = None
    for qs in faqs:
        cleaned_qs = clean_text(str(qs))
        score = fuzz.partial_ratio(user_ip_clean, cleaned_qs)
        if score > max_score:
            max_score = score
            best_qs = qs
    return best_qs, max_score

def writeHistory(txt):
    with open("chat_history.txt", "a") as f:
        f.write(txt + "\n")
