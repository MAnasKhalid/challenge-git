from jqqb_evaluator.evaluator import Evaluator
rule_json = {
    "condition": "AND",
    "rules": [{
        "id": "tagname",
        "field": "tags.name",
        "type": "string",
        "input": "text",
        "operator": "not_contains",
        "value": "production"
    }, {
        "id": "tagname",
        "field": "tags.name",
        "type": "string",
        "input": "text",
        "operator": "begins_with",
        "value": "development"
    }, {
        "condition": "OR",
        "rules": [{
            "id": "type",
            "field": "type",
            "type": "string",
            "input": "text",
            "operator": "equal",
            "value": "ec2"
        },{
            "id": "type",
            "field": "type",
            "type": "string",
            "input": "text",
            "operator": "equal",
            "value": "ami"
        }]
    }]
}


evaluator = Evaluator(rule_json)
object_1 = {'type': "ec2", "tags": [{"name": "hello"}, {"name": "asdfasfproduction_instance"}]}
object_2 = {'type': "ami", "tags": [{"name": "development"}, {"name": "asfdafdroduction_instance"}, {"name": "proction"}]}
objects = [object_1, object_2]

print(evaluator.get_matching_objects(objects))