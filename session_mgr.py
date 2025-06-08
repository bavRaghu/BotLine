# session_mgr.py

class SessionManager:
    def __init__(self):
        self.history = []
        self.active = "bot"
        self.status = None

    def add(self, sender, msg):
        self.history.append(f"{sender}: {msg}")

    def get_history(self):
        return self.history

    def set_active(self, who):
        self.active = who

    def get_active(self):
        return self.active

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
