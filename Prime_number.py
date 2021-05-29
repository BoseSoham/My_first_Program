number =  1981247

flag = 0
for i in range (2 , number) :
    if( number % i == 0 ) :
        print(number , "is not prime")
        print(i)
        flag = 1
        break
    
if (flag == 0):
    print(number , "is prime")
       
        