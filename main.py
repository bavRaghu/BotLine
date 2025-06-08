from dbMgmt import get_ans, get_client_name, insert_session, get_all_faqs
from utils import match_score
from session_mgr import SessionManager

faqs = get_all_faqs()
mgr = SessionManager()
company_name = get_client_name()
print(f"Bot: Hey! Welcome to {company_name} chat support. How may I help you?")
while True:
    user_ip = input("You: ")
    mgr.add("You", user_ip)
    if user_ip in ["bye", "exit", "quit"]:
        msg = "Thank you for chatting with us. Have a great day!"
        print("Bot: " + msg)
        mgr.add("Bot", msg)
        if mgr.get_active() == "bot":
            mgr.set_status("resolved")
        else:
            mgr.set_status("escalated")
        insert_session(mgr)
        break
    if mgr.get_active() == "bot":
        qs, score = match_score(user_ip, faqs)

        if score > 70:
            ans = get_ans(qs)
            print("Bot: " + ans)
            mgr.add("Bot", ans)
        else:
            msg = "I'm unsure about this. Connecting you to a customer service rep..."
            print("Bot: " + msg)
            mgr.add("Bot:", msg)
            mgr.set_active("rep")
            mgr.set_status("escalated")

    # elif mgr.get_active() == "rep":
    #     rep_response = input("Rep: ")
    #     print("Rep:", rep_response)
    #     mgr.add("Rep", rep_response)





