import re
from rapidfuzz import fuzz
import random

sessions = set()

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower().strip())

def match_score(user_ip, faqs):

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

def gen_session_id():
    while True:
        session = 'session' + str(int(random.random() * 100))
        if session not in sessions:
            sessions.add(session)
            return session

