a=input("Enter a string :")
find_wrd=input("Enter a string to be replaced :")
replace=input("Enter a string to be replaced :")
n=a.find(find_wrd)
if n!=-1:
    while(n!=-1):
        s=a[0:n]
        s+=replace
        s+=a[n+len(find_wrd):]
        a=s
        n=s.find(find_wrd,n+1,len(a))
else:
    print("The word does not exits")
print(a)
