from utils import readFAQS, matchScore
from session_mgr import SessionManager

faqs = readFAQS()
mgr = SessionManager()
print("Bot: Hey! Welcome to {company_name} chat support. How may I help you?")
while True:
    user_ip = input("You: ")
    mgr.add("You", user_ip)
    if user_ip in ["bye", "exit", "quit"]:
        msg = "Thank you for chatting with us. Have a great day!"
        print("Bot: " + msg)
        mgr.add("Bot", msg)
        break
    if mgr.get_active() == "bot":
        qs, score = matchScore(user_ip, faqs)
        if score > 50:
            ans = faqs[qs]
            print("Bot: " + ans)
            mgr.add("Bot", ans)
        else:
            msg = "I'm unsure about this. Connecting you to a customer service rep..."
            print("Bot: " + msg)
            mgr.add("Bot", msg)
            mgr.set_active("rep")
    elif mgr.get_active() == "rep":
        rep_response = input("Rep: ")
        print("Rep:", rep_response)
        mgr.add("Rep", rep_response)





