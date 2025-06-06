from utils import readFAQS, matchScore, writeHistory

faqs = readFAQS()

print("Bot: Hey! Welcome to {company_name} chat support. How may I help you?")
while True:
    user_ip = input("You: ")
    writeHistory("You: " + user_ip)
    qs, score = matchScore(user_ip, faqs)
    if score > 50:
        ans = faqs[qs]
        print("Bot: " + ans)
        writeHistory("Bot: " + ans)
    else:
        print("I'm unsure about this. Connecting you to a customer service rep...")
        writeHistory("Bot: " + "I'm unsure about this. Connecting you to a customer service rep...")
        break




