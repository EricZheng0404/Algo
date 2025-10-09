test = {
        "Key1" : "1",
        "Key2" : {
            "a" : "2",
            "b" : "3",
            "c" : {
                    "d" : {"x":{"y": "10"}},
                    "e" : "1"
                }
            }
        }

def flatten(test):
    res = {}
    helper(test, res, "")
    return res

def helper(test, res, path):
    for key, value in test.items():
        if isinstance(value, dict):
            helper(value, res, path + key + ".")
        else:
            res[path + key] = value
print(flatten(test))