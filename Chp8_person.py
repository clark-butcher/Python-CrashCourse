# def build_person(first_name,last_name):
#     person = {'first':first_name,'last':last_name}
#     return person
# muscian = build_person('jimi','hendrix')
# print(muscian)

def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
muscian = build_person('jimi','hendrix',age=27)
print(muscian)