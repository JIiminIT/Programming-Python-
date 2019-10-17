#239
import pickle
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름 : " + self.name + "\n나이 : " + str(self.age))


f = open("person_data.bin","wb")
p = Person("강지민",18)

pickle.dump(p,f)
f.close()

#rode
f = open("person_data.bin", "rb")
person = pickle.load(f)
print(person)

f.close()

#240

p1 = Person("지민",18)
p2 = Person("현수",18)
p3 = Person("예린",18)

persons = [p1,p2,p3]
f = open("persons_data.bin", "wb")
pickle.dump(person,f)
f.close()

