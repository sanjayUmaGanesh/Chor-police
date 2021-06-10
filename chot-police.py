import random
import pywhatkit

charectors = ['King', 'Queen', 'Mininster', 'Police', 'Theif', 'Guard', 'Peasent']
monkeys = ['Raji', 'Rama', 'Uma', 'Sriram', 'Aishu', 'Sneha', 'Ganesh' ]

 

for i in range(0,7):
    n = random.choice(monkeys)
    c = random.choice(charectors)
    charectors.remove(c)
    monkeys.remove(n)
    print(n + ' is the ' + c)
  
    
    
    
    




