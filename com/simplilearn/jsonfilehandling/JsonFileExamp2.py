import json

with open("file1.json",'r') as f :
    data1=json.load(f)
    print(data1)

    print(data1['name'])
    print(data1['email'])
    print(data1['phone'])
    print(data1['subject'])
    print(data1['subject'][0])
    print(data1['subject'][1])
    print(data1['subject'][2])
    print(data1['subject'][3])