print("\nTUPLES PRACTICE")

tup1 = (1,2,3,4,5)
print(f"I'm a {type(tup1)}. \n=> {tup1}")

tup2 = (6,7,8,9,10)
print(f"I'm a {type(tup2)}. \n=> {tup2}")

tup = tup1 + tup2
print(f"I'm a {type(tup)}. \n=> {tup}")

print("\nLISTS PRACTICE")

lst = list(tup)
print(f"I'm a {type(lst)}. \n=> {lst}")

lst1 = [10,20,30]
print(f"I'm a {type(lst1)}. \n=> {lst1}")

lst2 = [100,200,300]
print(f"I'm a {type(lst2)}. \n=> {lst2}")

lst = sum((lst1, lst2), lst)
print(f"I'm a {type(lst)}. \n=> {lst}")

dictionary = {'name': 'Ghalib Butt', "age": 24, "yob": 1998, "gender": "Male", "country": "Pakistan"}
print(dictionary)
