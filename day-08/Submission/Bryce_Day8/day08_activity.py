import csv
import json

#Reading csv file
with open("example1.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    firstColumn_values = [line[0] for line in csv_reader] #Prints only the first column of csv file
    print(firstColumn_values)

#Reading json file
with open("example2.json", "r") as json_file:
    json_data = json.load(json_file)

    print("")
    print(json.dumps(json_data, indent=2))