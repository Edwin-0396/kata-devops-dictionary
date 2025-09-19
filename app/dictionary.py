class Dictionary:
    def __init__(self):
        # Simple in-memory store
        self.entries = {}

    def newentry(self, word, definition):
        """
        Add a new word with its definition.
        If the word exists, update its definition.
        """
        self.entries[word] = definition

    def look(self, word):
        """
        Return the definition if the word exists,
        otherwise return a friendly message.
        """
        return self.entries.get(word, f"Can't find entry for {word}")