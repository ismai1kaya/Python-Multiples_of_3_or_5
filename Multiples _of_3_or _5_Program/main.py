#https://github.com/ismai1kaya

list1 = []
sum = 0
for  i in range(1000):
    if(i % 3 == 0 or i % 5 ==0 ):
        list1.append(i)
        sum +=i
        
print("Multiples of 3 or 5 are {}".format(list1))
print("Sum is",sum)
