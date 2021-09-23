
import configparser
import json

config = configparser.ConfigParser()
config.read('example.ini')

d = {}

for section in config.sections():
    print(section)
    d_section = {}
    for key in config[section]:
        d_section[key] = config[section][key]
    d[section] = d_section

print(d)

with open('output.json', 'w') as json_file:
    json.dump(d, json_file)