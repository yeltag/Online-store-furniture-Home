import json

with open(r'c:\Users\TaghiyevaYel\VisualStudio projects\app1\fixtures\goods\cats.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        print(item['fields']['name'])  # Should show Russian text