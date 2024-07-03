my_list = [10, 20, 30, 40, 50]
del my_list[0]
print(my_list)
# print(my_list[::-1])

# print(my_list[1:4])
#sets
my_fav = {"blue","black","white","red","green"}
her_fav = {"purple","white","red","blue","pink"}
all_favs = my_fav | her_fav #piping to unionize the sets
common_colors = my_fav & her_fav #finds commonalities
differences = her_fav.difference(my_fav) #finds differences
print(differences)

my_fav_color = ("blue", "red", "green", "white")
my_fav_list = list(my_fav_color)
my_fav_list.append("yellow")
my_fav_list[1] = "pink"
print(my_fav_list)