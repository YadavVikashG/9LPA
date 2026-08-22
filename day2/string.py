name="vikash"
print(name)
print(name[-5:-1])
#revers string
print(name[1::3])#only tack letter 1 and 4
print(name[::-1])
print(name[1:4])#only tack letter 1,2,3
text="this is vikash"
print(text.upper())#THIS IS VIKASH
print(text.lower())#this is vikash
print(text.capitalize())#This is vikash
print(text.replace("vikash","jaisey"))#only replace not change the actual word
word=text.split()
print(word)
languages = ["Python", "Java", "C++"]
wordjoin="-".join(languages)
print(wordjoin)
name="J"+name[1:]
print(name)

