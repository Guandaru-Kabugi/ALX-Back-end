# my_fruits = ["avocado", "oranges","bananas", "apples"]
# print(my_fruits[1])


# my_book = {
#     "Title":"The Wall Speaks",
#     "Author":"Jerr",
#     "Genre": "Self-Improvement"
# }
# Title = my_book.get("Title") #gets a specific value from a key
# print(Title)
# print(my_book["Author"])
# keys = my_book.keys() #collects all keys inside a dictionary
# keys = list(keys)
# keys[0]
# print(keys[0])
# values = my_book.values() #collects all values inside a dictionary
# print(values)
import random
#we start with a list
first_list =[]
second_list = [] 
third_list = []
#create a for loop to generate random numbers
for _ in range (5):
    random_number = random.randint(1,10)
    random_number2 = random.randint(1,10)
    random_number3 = random.randint(1,10)
    first_list.append(random_number)
    second_list.append(random_number2)
    third_list.append(random_number3)
#print the lists
print(first_list,second_list,third_list)
#convert the lists into sets
unique_set_1 = set(first_list)
unique_set_2 = set(second_list)
unique_set_3 = set(third_list)
#print the sets
print(unique_set_1,unique_set_2,unique_set_3)
#unionize the sets into one set
combined_sets = unique_set_1.union(unique_set_2,unique_set_3)
print(combined_sets)
