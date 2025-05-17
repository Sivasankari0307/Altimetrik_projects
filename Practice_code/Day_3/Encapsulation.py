# eNcapsulation
class text:
    def __init__(self, name):
        self._name = name
        self.__name = name

    def get_name(self):
        return self._name   
    def set_name(self, name):
        self._name = name
    def __str__(self):
        return f"Name: {self._name}"
    def __len__(self):
        return len(self._name)
    def __add__(self, other):
        return self._name + other._name
    def __eq__(self, other):
        return self._name == other._name
    
# Example usage
t1 = text("Anirudh")
t2 = text("Siva")
print(t1)   
print(len(t1))    
print(t1 + t2)   
print(t1 == t2)   

print(t1.get_name()) 
t1.set_name("Hari")  
print(t1.get_name()) 
print(t1._name)  






