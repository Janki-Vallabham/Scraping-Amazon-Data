import csv
import json

def csvConvert(csv_path,json_path):
    jsonData={}
    with open(csv_path,encoding="utf=8") as csvfile:
        csvData=csv.DictReader(csvfile)

        for rows in csvData:
            key=rows['Product Name']
            jsonData[key]=rows

    with open(json_path,'w',encoding='utf=8') as jsonfile:
        jsonfile.write(json.dumps(jsonData,indent=5))
    print("Data Convert")


csv_path='amazon_bags.csv'
json_path='amazon_bags.json'

csvConvert(csv_path, json_path)