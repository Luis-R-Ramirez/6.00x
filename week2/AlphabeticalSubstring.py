__author__ = 'luis'


#s = "ysofxauipsjpixhy"

s = 'abcdefgzabcdegijlmnpqr'
long= ''
lastlong = ''
longest = ''
last = 0
for i in s:

    if last < i:
        long = long + i


    print(last,i)
    if last >= i:
        #print(long)
        if len(long) > len(lastlong):
            print(long)
            longest = long
            lastlong = long
            long = i

        else:
            long = i

    last = i

if (len(long)>len(longest)):
    longest=long

print(longest)

