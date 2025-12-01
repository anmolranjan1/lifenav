# memory/memory_bank.py

class MemoryBank:
    def __init__(self):
        self.long_term = {}

    def save_preference(self, key, value):
        self.long_term[key] = value

    def get_preference(self, key):
        return self.long_term.get(key)
