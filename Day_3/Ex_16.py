class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price          
        
    def __gt__(self, other):
        return self.price > other.price
    
    def __str__(self):
        return f"{self.name} {(self.price)} ฿"

prod1 = Product("Phone", 50000)
prod2 = Product("Airpod", 5000)

print(prod1 > prod2)  
print(prod2 > prod1)  