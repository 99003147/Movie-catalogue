import re 
   
p = re.compile('[a-e]') 
  
print(p.findall("What is going on, buddy")) 
   
#Output- [a, b, d, d]
