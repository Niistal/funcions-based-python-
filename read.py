import os
f=open("testua2.txt", "a")
#a append, r read, write
s=input("Write the text you want to add")
f.write(s)
f.write("\n")
s2=input("Write another line")
f.write(s2)
f.write("\n")
f.close()
f=open("testua2.txt","r")
a = 1
while a!=0:
   file_line = f.readline()
   if not file_line:
       print("End Of File")
       a = 0
   else:
       print(file_line)
       a=a+1
f.close()
#a esta para guardar y r para leer pero con la w reinicia todo tu documento y hace que escribas otra vez