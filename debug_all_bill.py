from moduletest_for_import import classifier, hospitalfinder
import json
import os


def text_concat(json_data):
    text = " ".join([str(text.get('text')) for text in json_data])
    return text  # os.getcwd()


print(os.getcwd())
rawDataf = open("all_bill.json")
print(str(rawDataf))
rawData = json.load(rawDataf)
print(rawData)

# print(rawData)
hospital_id = "none"
docs = []
for i in rawData:
    # print(rawData[i])
    text_json = text_concat(rawData[i])
    print(text_json)
    hospital_id = hospitalfinder(text_json)
    if hospital_id != "none":
        break
for i in rawData:
    text_json = text_concat(rawData[i])
    doc = classifier(text_json, 2, hospital_id, 0, i)
    docs.append(doc)
print(hospital_id)
print(docs)
