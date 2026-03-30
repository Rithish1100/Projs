import pandas

# data=pandas.read_csv("weather_data.csv")
# #print(type(data))
# #print(type(data["temp"]))

# # data_dict=data.to_dict()
# # print(data_dict)

# # temp_list=data["temp"].to_list()
# # print(len(temp_list))

# # print(data["temp"].mean())
# #print(data["temp"].max())

# # print(data.condition)
# # print(data[data.day=="Monday"])

# # print(data[data.temp==data["temp"].max()])

# # monday=(data[data.day=="Monday"])
# # monday_ferhenite=(monday.temp*9/5)+32   
# # print(monday_ferhenite)

# data_dict={
#     "students":["amy","james","jessi"],
#     "score":[74,45,33]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_data_csv")
# print(data)
squirell_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260330.csv")
squirell_gcolor_count=len(squirell_data[squirell_data["Primary Fur Color"]=="Gray"])
squirell_ccolor_count=len(squirell_data[squirell_data["Primary Fur Color"]=="Cinnamon"])
squirell_bcolor_count=len(squirell_data[squirell_data["Primary Fur Color"]=="Black"])
squirell_data_dict={
    "Fur color":["Grey","Cinnamon","Black"],
    "Count":[squirell_gcolor_count,squirell_ccolor_count,squirell_bcolor_count]
    }

df=pandas.DataFrame(squirell_data_dict)
df.to_csv("Squirell_color_count.csv")