from lettermatrix import *


#testing
m = letterMatrix(10,9)

nm = addWord(3,4,False,'hej',m)
if nm != False:
    m = nm

nm = addWord(6,3,False,'boll',m)
if nm!= False :
    m = nm

nm = addWord(3,4,True,'hoho',m)
if nm != False:
    m = nm

nm = addWord(6,0,True,'cake',m)
if nm != False:
    m = nm

printMatrix(m)
