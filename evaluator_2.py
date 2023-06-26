from jqqb_evaluator.evaluator import Evaluator

rule_json =  {
    'condition': 'OR',
    "rules": [
      {'id':"age","type":'number',"input": "text",      "field": 'age', "operator": 'greater_or_equal', "value": 10},
      {'id':"gender","type":'string',"input": "12",   "field": 'gender', "operator": 'contains', "value": 'f'},
# {'id':"gender2","type":'string',"input": "text",   "field": 'gender2', "operator": 'equal', "value": 'f'}
    ]
  };

evaluator = Evaluator(rule_json)
object_1 = {'age': 9, 'gender':'m'}
object_2 = {'age':9, 'gender':'f'}
objects = [object_1, object_2]

print(evaluator.get_matching_objects(objects))