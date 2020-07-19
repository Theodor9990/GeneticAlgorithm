

"This is a genetic algorithm that aims to deermine the maximum global of a function of n variables subjected to one constraint"

import random 

#create the initial list

class Variables:
    
    def __init__(self, value):
        
        self.numb_item = [ _ for _ in range(value)]
        self.weight = [random.randint(1,100)/10 for _ in range(value)]
        self.value = [random.randint(1,100) for _ in range(value)]
    
    #def __str__(self):
       #return [[self.numb_item], [self.weight], [self.value]]

                
shop = Variables(10)
shop = [shop.numb_item, shop.weight, shop.value]

solution_per_population = 8
pop_size = (solution_per_population, shop[0])



