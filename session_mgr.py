class SessionManager:
    def __init__(self):
        self.history = []        # Stores all chat messages
        self.active = 'bot'      # Tracks who's replying: 'bot' or 'rep'

    def add(self, sender, msg):
        self.history.append(f"{sender}: {msg}")

    def get_history(self):
        return self.history

    def set_active(self, who):
        self.active = who

    def get_active(self):
        return self.active
