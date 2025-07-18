# s = {1,2,3,2,4}
# print(s)

# d=set()
# d.add(5)
# print(d)

# s1={1,2,3}
# s2={3,4,5}
# print(s1.union(s2))
# print(s1.intersection(s2))

# fs = frozenset([1,2,3,3,2])
# print(fs)

# s={frozenset([1,2]), frozenset([3,4])}
# print(s)

# from collections import defaultdict
# d2 = defaultdict(list)
# d2['x'].append(10)
# print(d2)

try:
 num = int(input("Enter a number: "))
 result =10 / num
 print("Results is: ",result)

except ZeroDivisionError:
    print("Cannot Divide by zero")
except ValueError:
    print("Invalid Input,please input a number")
    