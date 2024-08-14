n=5
i=0
fact=1
while i!=5:
    fact*=n-i
    i+=1
print(fact) 


x="abcdefghijklmnop"
i=0
let=" "
while x[i]!="o":
    if x[i]=="a":
        let="a"
    elif x[i]=="m":
        let+="m"
    elif x[i]=="j":
        let+="j"
if len(let)==3:
    print("true")
else:
    print("false")
