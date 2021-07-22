import numpy as np
import re
import matplotlib.pyplot as plt
'''
open() take 2 arguments file name and mode
    read() to read content of the file
	need encoding ="utf8" to read text file



'''

# open file txt
f = open("N.txt","rt",encoding="utf8")
x= f.read()
f.close()
# x= x.lower()

# x = x.title()
# x = x.center(50)
# x = x.index("thích")
print(len(x))
# fi = re.findall("[a-z]",x) #result list all element from a to m
# for value in fi :
#  	print(value,end=" ")

# g = re.findall("\d",x)
# print(g)                 #['3']
#|^	|Starts with	|"^hello"	
#|$	|Ends with		|"world$"
'''
check if string starts with "^   " 
g = re.findall("^Trong",x)
if g :
	print("True")
else:
	print("false")


'''

fi = re.findall("t*",x) #find all element "ta"
# print(fi)

# gi = re.findall("xâ{2}", x)
# print(gi)
# for idx,i in enumerate(x):
# 	print(idx,i)

import numpy.random as rd
y = np.arange(1,len(fi)+1)
fi = np.array(fi)


if len(fi)==len(y):
	plt.plot(fi,"*",c = "r")
	plt.title("Tan suat xuat hien chu cai t")
	plt.show()

