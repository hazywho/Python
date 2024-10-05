#task1
for i in range(6):
    print("data")
#task2
friends = ["joseph", "glenn", "sally"]
for p in friends:
    print(f"happy new year: {p}")
print("Done")
#task3
count = 0
for it in [3,41,12,9,74,15]:
    count+=1
print(count)
#task4
total = 0
for i in [3,41,12,9,74,15]:
    total += i
print(total)
#task5
largest = None
print(f"Before: {largest}")
for i in [3,41,12,9,74,15]:
    if largest<i:
        largest=i
print(f"After: {largest}")
#task6
smallest = None
print('Before:', smallest)
for itervar in [3,41,12,9,74,15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:',itervar,smallest)
print('Smallest:',smallest)
#task7
num = int(input('Enter a number:'))
for i in range(1,13):
    print(i, 'x', num , '=', num *i)