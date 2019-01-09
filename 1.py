from math import sinh
from math import atanh

a = float (input ("a:"))
x = float (input ("x:"))

G = -(3*(14*(a*2)+23*a*x-30*(x*2)))/(-9*(a*2))+37*a*x+40*(x*2))
F = -tan(18*(a*2)-a*x-4*(x*2))
Y = (log(35*(a*2)-27*a*x+4*(x*2)+1))/(log(2))

print ("G=""%2f" %G)
print ("F=""%2f" %F)
print ("Y=""%2f" %Y)
