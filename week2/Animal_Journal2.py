from Animals2 import Animal2, Dog2, Cat2, Horse2  # importing animals class to the Animal module
import re
# d1 = Dog("Fido", 10, "brown")
# print(d1)
# d1.sleep()
# d1.move()
# d1.getOlder(1)
# print(d1)

# c1 = Cat("Garfield", 15, "orange")


# d1 = Dog("Fido", 10, "brown")
# c1 = Cat("Garfield", 15, "orange")

# lst_Animals = [d1, c1]
# for animal in lst_Animals:
#     animal.sleep()
#     animal.move()
#     animal.getOlder(3)
#     print(animal)

# print(c1.color)

#TODO : Exception handling, persist data (file input/out)
# Stretch goal: Be able to modify animals, call methods




def main():

    print("***WELCOME TO THE ANIMAL JOURNAL! ***")
    
    fname = "all_animals2.csv" #file name 
    lst_animals = []

    lst_animals = load_animals(fname)


    while(True):                      #infinite loop which is why break is needed
        animal = insert_animal()
        if animal == None:
            break

        lst_animals.append(animal)
    
    print("\n\n**** ALL animals****")
    for elem in lst_animals:
        print(elem)
    
    save_animals(fname, lst_animals)
    print("\n\n")

    '''
    save_animals

    This function will take in a list of animals and save them to a csv file.

    Returns None
    '''


def save_animals(fname, lst_animals):
    with open(fname, "w") as f:
        for animal in lst_animals:
            if type(animal) == Cat2:
                f.write("Cat," + animal._name + "," + str(animal._age) + "," + animal._color + ",\n")
            
            elif type(animal) == Dog2:
                
                f.write("Dog," + animal._name + "," + str(animal._age) + "," + animal._color + ",\n")
           
            elif type(animal) == Horse2:
                
                f.write("Horse," + animal._name + "," + str(animal._age) + "," + animal._color + ",\n")
            else:
                pass


def load_animals(fname) :

        ''''
        load_animals

        This function will take in a file name representing a csv file of animals to load into an animal list

        Returns list of Animals
        '''
        lst_animals =[]
        
        with open(fname, "r") as f:
            for line in f:
                info = line.split(',')
                if info[0] == "Cat":
                    animal = Cat2(info[1], info[2], info[3])
                elif info[0] == "Dog":
                    animal = Dog2(info[1], info[2], info[3])
                elif info[0] == "Horse":
                    animal = Horse2(info[1], info[2], info[3])
                else:
                    animal = None
            
                if animal != None:
                    lst_animals.append(animal)
    
        return lst_animals


def insert_animal() -> Animal2:
    '''
    insert-animal

    This function prompts the user for information about what animal to insert into the journal

    Returns Animal
    Retruns None if the user wants to quit
    '''
    print("\nPlease select which animal you want to enter into the journal:")
    print("\t1)Cat")
    print("\t2) Dog")
    print("\t3) Horse")
    print("\t4) quit")
    animal_type = input(">>> ")

    #  Break out of function if user wants to quit!!

   # if animal_type == "4":
    if animal_type not in ["1", "2", "3",]:
        return None

    
    # name= str(input("\nEnter Animal's name: \n>>>"))
    # age = int(input("\nEnter Animal's Age: \n>>>"))
    # color = str(input("\nEnter Animal's Color: \n>>>"))

    while True:
            try:
                name = input("\nEnter animal's name: \n>>>")
                check = re.search(',', name)
            
                if check != None:
                    raise ValueError
            except ValueError as ve:
                print("\nCANNOT HAVE COMMAS IN NAME")
            else:
                break


    
    while True:
         try:
             age = int(input("\nEnter animal's age:\n>>>"))
         except ValueError as ve:
             print("\nCANNOT ENTER A STRING FOR AGE! PLEASE ENTER AN INTEGER!\n")
         else:
             break 

    
    while True:
        try:
            color = input("\nENter animals's color: \n>>>")
            check = re.search(',', color)

            if check != None:
                 raise ValueError
        except ValueError as ve:
             print("\nCANNOT HAVE COMMAS IN COLOR!\n")
        else: 
             break

    
    if animal_type == "1":
        animal = Cat2(name, age, color)
    elif animal_type == "2":
        animal = Dog2(name, age, color)
    elif animal_type == "3":
        animal = Horse2(name, age, color)
    else: 
        animal = None
    
    return animal
   # print(animal)
    #pass

if __name__ == "__main__":
    main()