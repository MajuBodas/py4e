text = "X-DSPAM-Confidence:    0.8475"


a = text.find('5')
e = text.find('0')

c=int(a)
d=int(e)

b = text[d:c+1]

f=float(b)

print(c)
print(d)
