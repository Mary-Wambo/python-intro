# loops
# repeat
#for loop
for number in  range (11):
    result= number ** 2
    if result % 2 != 0:
        print(number,"tok")

    result=number ** 2
    if result % 2 == 0:
     print(number, "tik")
#create another loop that will print the following
#if the number is odd print the word 'tik' + number
#if the number is even print 'tok' + number
#15 tik
#16 toktok

print("multiplication table (1 to 10)")
for i in range (1,11):
    print(f"{i} x {i} ={i*i}", end=print()  )#newline after each row

for i in range(10):
    for j in range(2,1):
        if i%j==0:
            break
        else:
            print(i)

    for number in reversed(range(1,10)):
        print(number)




