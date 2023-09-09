n1=int(input())
n2=int(input())
for num in range(n1,n2+1):
        count = 0
        delitel = 2
        while delitel<num:
            if num%delitel == 0:
                count += 1
            delitel += 1
        if count == 0 and num!=1:
            print (num)
