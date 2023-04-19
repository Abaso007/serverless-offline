import json

def hello(event, context):
    data = [
        {"a": x, "b": True, "c": 1234567890, "d": "foo"} for x in range(1000)
    ]
    return {
        "body": json.dumps(data),
        "statusCode": 200
    }
