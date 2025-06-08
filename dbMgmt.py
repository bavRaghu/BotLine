from datetime import datetime
from pymongo import MongoClient
from utils import gen_session_id
from consts import uri

client = MongoClient(uri)

db = client["BotLine"]


def get_all_faqs():
    faqs = db.faqs.find({}, {"_id": 0, "question": 1})
    return [faq["question"] for faq in faqs]


def get_ans(qs):
    res = db.faqs.find_one({"question": qs}, {"_id": 0, "answer": 1})
    return res["answer"]


def get_client_name():
    res = db.faqs.find_one({"client_id": "client1"}, {"client_name": 1, "_id": 0})
    return res["client_name"] if res and "client_name" in res else "Not found"



def insert_session(sm):
    session_data = {
        "session_id": str(gen_session_id()),
        "timestamp": datetime.utcnow().isoformat(),
        "chat_history": sm.get_history(),
        "status": "resolved" if sm.get_active() == "bot" else "escalated",
        "handoff_required": sm.get_active() == "rep"
    }
    db.sessions.insert_one(session_data)
