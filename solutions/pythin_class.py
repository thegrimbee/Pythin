class Pythin:
    def __init__(self, items, stomach_size = 3):
        self.items = items
        self.status = "ongoing"
        self.items_eaten = 0
        self.stomach = []
        self.swallow_count = 0
        self.STOMACH_SIZE = stomach_size
        self.moves = []

    def is_full(self):
        return len(self.stomach) == self.STOMACH_SIZE
    
    def get_items(self):
        return self.items
    
    def peek_stomach(self, ):
        return self.stomach.copy()

    def eat(self, item):
        if self.status == "ongoing":
            self.moves.append(item)
            self.items_eaten += 1
            if len(self.stomach) < self.STOMACH_SIZE: 
                self.stomach.append(self.items[item])
            else:
                self.status = "stomach overflow"

    def swallow(self):
        if self.status == "ongoing":
            self.moves.append("S")
            self.swallow_count += 1
            if self.stomach.count("tiger") > 1:
                self.status = "tiger overflow"
            else:
                self.stomach = []
                if self.status == "ongoing" and self.items_eaten == len(self.items):
                    self.status = "success"

