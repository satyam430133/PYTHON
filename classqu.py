'''
Write a  class named animal constructed by a name, no_legs, category
(herbivores, carnivores and omnivores)and
private data member: name(string type),no_legs (int type),category(string type) (herbivores, carnivores and omnivores)
detail(string type)
private member function:
    void set_detail()
description:
 1)herbivores -> "animals that eat plants"
 2)carnivores -> "animals that eat only meat"
 3)omnivores -> "animals eat both plants and meat"  
public 
member function: parameterized_constructor(name,legs,category)
                  and call set_detail() inside it.
                  all_details() -->display all
                  category () -->display category
Create some objects and display result.
'''
class animal:
    def __init__(self,name,legs,category):
        self.name = name
        self.legs = legs
        self.category = category
        self.details = ''
        self.setDetails()
    def setDetails(self):
        if self.category == "herbivores":
            self.details = "Animals That Eat Plants"
        elif self.category == "carnivores":
            self.details = "Animals That Eat Only Meat"
        elif self.category == "omnivores":
            self.details = "Animal That Eat Both Plants & Meat"
    def allDetails(self):
        print("Name :", self.name)
        print("Number of Legs :", self.legs)
        print("Category :", self.category)
        print("All Details:", self.details)
    def category(self):
        print("Category",self.category)


sher = animal("Sher", 4, "carnivores")
hiran = animal("Hiran", 4, "herbivores")
bhalu = animal("Bhalu", 4, "omnivores")
rat = animal("Sher", 4, "carnivores")
cat = animal("Hiran", 4, "herbivores")
dog = animal("Bhalu", 4, "omnivores")

sher.allDetails()
# hiran.category()
# sher.category()
