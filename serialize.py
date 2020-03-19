import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s,default=lambda obj:obj.__dict__))#转换成dict，否则会报错
#结果：{"name": "小明", "age": 20}
#{"name": "Bob", "age": 20, "score": 88}