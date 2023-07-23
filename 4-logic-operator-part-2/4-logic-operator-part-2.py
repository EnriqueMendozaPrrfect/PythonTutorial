# Ademas de los operadores logicos vistos anteriormente (=, <, >, !) 
# tenemos los operadores and (&&) y or (||), los cuales permiten especificar
# la relación entre operadores logicos
# 
#      var x   |     var y      |    AND   |     OR      |
#  ____________|________________|__________|_____________|
#      TRUE    |      TRUE      |   TRUE   |    TRUE     |
#  ____________|________________|__________|_____________|
#      TRUE    |     FALSE      |  FALSE   |    TRUE     |
#  ____________|________________|__________|_____________|
#     FALSE    |      TRUE      |  FALSE   |    TRUE     |
#  ____________|________________|__________|_____________|
#     FALSE    |     FALSE      |  FALSE   |   FALSE     |
#  ____________|________________|__________|_____________|


print(True and True)
print(True or True)

print(True and False)
print(True or False)

print(False and True)
print(False or True)

print(False and False)
print(False or False)

print(5 > 3 and 6 > 5)
print(5 > 3 or 6 > 5)

text1 = 'hello'
text2 = 'world'

print(text1 == 'hello')
print(text1 == 'hello' and text1 == 'world')
print(text2 == 'hello' or text2 == 'world')

print(text1 == 'hello' and (text1 == 'world' or text2 == 'world'))
