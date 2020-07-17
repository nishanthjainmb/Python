import json

with open('newState.json','r') as statesjson:
    statesname=json.load(statesjson)
    # print(statesname)
# for state in statesname['states']:
#     print(state['abbreviation'])

for state in statesname['states']:
    del state['abbreviation']

with open('newstate.json','w') as newstatename:
    json.dump(statesname,newstatename,indent=2)