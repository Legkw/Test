class inmemory:
    def __init__(self, dictionary = {}):
        self.DB = dictionary
	
    def add(self, item):
        item.id = len(self.DB)
        self.DB[item.id] = item
	
    def get(self, ix):
        return self.DB[ix]
        
    def delete(self, ix):
        del self.DB[ix]
        