import yaml

with open('data.yaml') as f:
    datas=yaml.load_all(f, Loader=yaml.FullLoader)
    for data in datas:
        for k , v in data.items():
            print(k, "->" , v)
