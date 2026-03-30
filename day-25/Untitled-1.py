#with open("weather_data.csv") as wdata:
#    data=wdata.readlines()
#    print(data)

import csv

with open("weather_data.csv") as data_file:
    data=csv.reader(data_file)
    temperature=[]
    for rows in data:
        if rows[1] !="temp":
            temperature.append(rows[1])
print(temperature)