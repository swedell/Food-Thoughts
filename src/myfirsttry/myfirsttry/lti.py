temp = 0 
while (True):   
   n = input()
#    n = n + n[::-1]
#    print(n[::-1])
   v = str(n)
   temp = v[::-1]
   if v == temp : 
       print("palindrom hai  ")
       break 
   else  :
       continue 