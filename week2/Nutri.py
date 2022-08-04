# ******* JOURNAL APP********
#Data should be read and written to CSV(comma, seperated, vales) or JSON files

#Command Line Interface where users can interact with the application while its running
#Application should read in data from a file and be displayed in some way
#Application should write data to a file
#All user input should be validated (program should not end with exceptions based on user input)
#Program must follow OOP design (classes/objects)
#Application should be uploaded to a GitHub repo.


#Personal Obj
#Nutri journal app to record/track nutrional information
#Records food item and nutrients info
#Nutrients = calories, fat, vit, carbs, proteins, sodium, sugar
#records nutrients and food name in file
#messages can exclaim when proceeding over daily limit



class Nutrition():
    def __init__(self, food_item, calorie, fat, carb, protein, sodium, sugars=""):
        self.food_item = str(food_item)
        self.calorie = int(calorie)
        self.fat = int(fat)
        self.carb = int(carb)
        self.protein = int(protein)
        self.sodium = int(sodium)
        self.sugars = int(sugars)

    def __str__(self): #overriding string default
        return "FOOD ITEM:" + self.food_item + ", Calories: " + str(self.calorie) + ", Fats: " + str(self.fat) + ", Carbs: " + str(self.carb) + ", Protein: " + str(self.protein) + ", Sodium: " + str(self.sodium) + ", Sugars: " + str(self.sugars)


class Breakfast(Nutrition):
    pass

class Lunch(Nutrition):
    pass

class Dinner(Nutrition): 
    pass
