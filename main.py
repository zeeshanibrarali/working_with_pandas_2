import pandas

data = pandas.read_csv("Free_Test_Data_500KB_CSV-1.csv")
name = data["NAME"].tolist()
age = data["AGE"].tolist()
country = data["COUNTRY"].tolist()
new_data = []
new_name = []
new_dict = {"names": [], "age": []}
new_dict2 = {"Great Britain": [], "France": [], "United States": []}
count = 0
for i in range(len(age)):
    if 20 <= age[i] <= 30:
        new_data.append(age[i])
        new_name.append(name[i])
        new_dict["names"].append(name[i])
        new_dict["age"].append(age[i])
        count += 1
    if country[i] == "Great Britain":
        new_dict2["Great Britain"].append(name[i])
    elif country[i] == "France":
        new_dict2["France"].append(name[i])
    elif country[i] == "United States":
        new_dict2["United States"].append(name[i])

#  printing age against their names
for i in range(len(new_data)):
    print(new_name[i], new_data[i])

# printing total number of values and number of values between the given range
print("total : ", len(data), "\nRange between 20 to 30 years old : ", count)

# printing in a form of dictionary of lists of above new data
print(new_dict.items())

# printing names respectively to their country
print(new_dict2.items())



