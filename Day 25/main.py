# # with open("weather_data.csv") as file:
# #     list1 = file.readlines()
# #     print(list1)
#
# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].tolist()
# # average = sum(temp_list)/len(temp_list)
# # print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(temp_list)
# print(data_dict)
#
# # Get data in columns
#
# print(data["condition"])
# print(data.condition)
#
# # Get data in rows
#
# print(data[data["temp"] == data["temp"].max()])
#
# Monday = data[data.day == "Monday"]
# temp_in_fahrenheit = Monday.temp * (9 / 5) + 32
# print(Monday.temp)
# print(temp_in_fahrenheit)
#
# # Create a dataframe from scratch
#
# data_dic = {
#     "students": ["abir", "arnab", "joy"],
#     "marks": [98, 99, 56]
# }
#
# data2 = pandas.DataFrame(data_dic)
# print(data2)
# data2.to_csv("new_data.csv")
import pandas

# Getting fur color

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240521.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
}
data1 = pandas.DataFrame(data_dict)
data1.to_csv("new_squirrel_data.csv")