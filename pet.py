class Pet:
    def __init__(self, name):
        
        #Pet's attributes

        self.name = name #Name of the pet
        self.hunger = 5 # Hunger level of the pet( 0 = full, 10 = starving)
        self.energy = 5 # Energy level of the pet (0 = tired, 10 = full of energy)
        self.happiness = 5 #Happiness level of the pet (0 = sad, 10 = happy)
        self.tricks = [] # List of tricks the pet can perform


    def eat(self):

        #The pet eats doof, reducing hunger and increasing happiness

        if self.hunger > 0:
            self.hunger = max (self.hunger -3, 0) #Reduce hunger by 3, but not below 0
            self.happiness = min (self.happiness + 1, 10) #Reduce happiness by 1, but not above 10
            print(f"{self.name} ate some food! Yum!")

        else:
            print(f"{self.name} is not hungry right now.")


    def play(self):

        #The pet play, increasing energy and happiness

        if self.energy >= 2:
            self.energy = max (self.energy - 2, 0) # Decrease energy by 2, but not below 0
            self.happiness = min (self.happiness + 2, 10)   # Increase happiness by 2, but not above 10
            self.hunger = min (self.hunger + 1, 10) # Increase hunger by 1, but not above 10
            print(f"{self.name} had so much gun playing!")

        else:
            print(f"{self.name} is too tired to play right now.")  

    def sleep(self):

        #The pet sleeps, increasing energy

        self.energy = min (self.energy + 5, 10) # Increase energy by 5, but not above 10
        print(f"{self.name} took a nap and feels refreshed!")


    def train(self, trick):

        #The pet learns a new trick

        self.tricks.append(trick) # Add the trick to the list of tricks
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
            
            #Display the tricks the pet has learned
    
            if self.tricks:
                print(f"{self.name} can do the following tricks")
                for trick in self.tricks:
                    print(f"- {trick}")
            else:
                print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        #Display the pet's status
        print(f"{self.name}'s status:")
        print(f"- Hunger: {self.hunger}/10")
        print(f"- Energy: {self.energy}/10")
        print(f"- Happiness: {self.happiness}/10")


