import json
import codecs

countries = []
allowed = ['United States', 'Canada']


def parse(data):
    features = data['features']
    for i in range(0, len(features)):
        if features[i]['properties']['name'] in allowed:
            countries.append(features[i])
            print(i)

    data['features'] = countries
    jsonStr = json.dumps(data)

    with codecs.open('world_4.json', 'w', 'utf-8') as w:
        w.write(jsonStr)


with codecs.open('world.json', 'r', 'utf-8') as f:
    js = json.loads(f.read())
    parse(js)
#print(len(js))
