class People:
    people = {}
    def __init__(self):
        self.people = dict()
        self.people["Marion"] = "Engineer"
        self.people["James"] = "Doctor"
        self.people["Frederick"] = "Accountant"
        self.people["John"] = "Lawyer"
    
    def search(self, word: str):
        if(word in self.people):
            return self.people.get(word)
        else:
            return "Person not found"

       
    
        

