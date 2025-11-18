import json
with open("rizz.json","r",encoding='utf-8') as f:
    data = json.load(f)
    for key in data:
        print(key,": ",data[key])
with open("inforn.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4, ensure_ascii=False))