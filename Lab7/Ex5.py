celebrities_tuple = ("Taylor Swift", "Lionel Messi", "Max Verstappen", "Keanu Reeves", "Angelina Jolie")
ages_tuple = (34, 36, 26, 59, 48)

celebrities_list = [celeb for celeb in celebrities_tuple]
ages_list = [age for age in ages_tuple]

celebrities_dictionary = {
    "celebrities": celebrities_list,
    "ages": ages_list
}
print(celebrities_dictionary)