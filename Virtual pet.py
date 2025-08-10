import random
import time

class Virtual_pet():

    def __init__(self,name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.alive = True

    def feed(self):
        if self.alive:
            self.hunger = min(100, self.hunger + 20)
            print(f"{self.name} is being fed,Hunger level:{self.hunger})")
        else:
            print(self.name, 'is no more!')

    def play(self):
        if self.alive:
            self.happiness = min(100, self.happiness + 20)
            self.hunger = max(0, self.hunger - 20)
            self.energy = max(0, self.energy - 10)
            print(f"{self.name} is playing. Happiness level: {self.happiness},Hunger level: {self.hunger},Energy level: {self.energy}")
        else:
            print(self.name,"is no more")

    def sleep(self):
        if self.alive:
            self.energy = min(100,self.energy + 30)
            print(f"{self.name} is sleeping. Energy level:{self.energy}")
        else:
            print(self.name,'is no more')

    def check_status(self):
        print('Status is: Hunger level:',self.hunger, 'Happiness level:', self.happiness,'Energy level:',self.energy )

    def pass_time(self):
        if self.alive:
            self.hunger = max(0,self.hunger - random.randint[5,10])
            self.happiness = max(0,self.happiness - random.randint[1,5])
            self.energy = max(0,self.energy - random.randint[3,7])

            if self.hunger or self.energy == 0:
                self.alive = False
                print(self.name,' has died ! You neglected it so much')
        
            else:
                print(f"{self.name}'s stats - Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}")
        else:
            print(f"{self.name}is no longer with us!")

def game_loop():
    print('Welcome to the Virtual pet game')
    name = str(input('Enter the name of your pet:  '))
    pet = Virtual_pet(name)
     
    while pet.alive:
        print("\nChoose an action:")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Check status")
        print("5. Quit game")

        action = input("Enter the number of your action: ")
        if action == '1':
            pet.feed()
        elif action == '2':
            pet.play()
        elif action == '3':
            pet.sleep()
        elif action == '4':
            pet.check_status()
        elif action == '5':
            print("You decided to quit the game. Goodbye!")
            break
        else:
            print('Invalid choice!')
        
    pet.pass_time()
    time.sleep(2)
if __name__ == '__main__':
    game_loop()

    
    

    






        
