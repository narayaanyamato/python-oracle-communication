import sys
from Bookmenu import Bookmenu
from BookOperations import Addbook,Updatebook,Removebook,Viewbook
try:

     while(True):
         Bookmenu()
         v = int(input("Enter your choice :"))
         print("-"*70)
         if(v==1):
             Addbook()
         elif(v==2):
             Removebook()
         elif(v==3):
             Updatebook()
         elif(v==4):
             Viewbook()
         elif(v==5):
             sys.exit()
         else:
             print("\u001b[31;1m"+"out of choice !")

except ValueError:
    print("\u001b[31;1m"+"invalid input")