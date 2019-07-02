s=list("the 43earthquick 21brown $fox")
alphabets=0
numbers=0
special=0
for i in s:
	if i.isalpha():
		alphabets=alphabets+1
	elif i.isdigit():
		numbers=numbers+1
	elif not i.isalnum() and i!=" ":
		special=special+1

print("alphabets: "+str(alphabets))
print("numbers: "+str(numbers))
print("special characters: "+str(special))			

