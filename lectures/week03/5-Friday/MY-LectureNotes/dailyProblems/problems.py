# Return a new list with each element multiplied by 5

nums = [56, 34, 34, 1, 1, 1, 23, 12, 89, 89, 89, 70, 56] 
new_list= []

for i in nums:
    new_list.append((i*5))
print(new_list)

# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).

l1 = [["name", "Elie"], ["job", "Instructor"]]
dic = {}

for i in range(len(l1)): 
    dic[l1[i][0]]=l1[i][1]
print(dic)        