"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
                    


s=[]
 
 
#for i in range(401):
#    s.append(0)
    
        
for i in range(400):
      
    if i == 0:
        s.append(1+1)
        
      
    elif i < 20 and i >0:
        s.append(1+ s[i-1])
        
    elif str(i)[-1:] == '0' :
        s.append(1 + s[i-20])
        
    else:    
        s.append( s[i-1] + s[i-20])
               
print s[399]