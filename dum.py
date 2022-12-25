def phone(n):
      alpha='abcdefghijklmnopqrstuvwxyz'
      code=''.join([str(alpha.find(c)+1) for c in n.lower() if c in alpha ])
      return code

message='hello we are the great encypters'
code=phone(message)
print(code)      
       
        

    
     


    