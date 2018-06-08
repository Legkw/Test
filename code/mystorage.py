class inmemory:
    def __init__(self, dictionary = None):
        if dictionary is None: dictionary = {}
        self.DB = dictionary
	
    def add(self, item):
        item.id = len(self.DB)
        self.DB[item.id] = item
	
    def get(self, ix = None):
        if ix is None:
            return list(self.DB.values())
        return self.DB[ix]
        
    def delete(self, ix):
        del self.DB[ix]
        