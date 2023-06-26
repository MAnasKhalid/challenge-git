from jqqb_evaluator.evaluator import Evaluator
import json

survey = json.load(open('survey.json'))

print("survey",)
for question in survey[0]['questions']:
    print(question)

rule_json = {
    'condition': 'AND',
    "rules": [
      {'id':"1.00","type":'string',"input": "", "field": 'options.label', "operator": 'equal', "value": 'Yes'},
      {'id':"2.00","type":'number',"input": "", "field": 'order', "operator": 'equal', "value": 1},
    ]
}

evaluator = Evaluator(rule_json)

survey = [{'id': 1, 'question': 'Does the Customer want to Change the Floorplan?', 'has_input': False, 'input_option': None, 'input_title': 'null', 'related_question': None, 'options': [{'id': 1, 'label': 'Yes'}], 'order': 1}, {'id': 2, 'question': 'Do we need to Remove Walls?', 'has_input': False, 'input_option': None, 'input_title': 'null', 'related_question': 1, 'options': [{'id': 1, 'label': 'Yes'}, {'id': 2, 'label': 'No'}], 'order': 2}]
# object_1 = {'age': 9, 'gender':'m'}
# object_2 = {'age':9, 'gender':'f'}
# objects = [object_1, object_2]

print(evaluator.get_matching_objects(survey))