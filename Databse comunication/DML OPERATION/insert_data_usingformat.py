import oracledb as orc
class NameError(Exception):pass
def Namechk(name):
    w=name.split()
    res=False
    for i in w:
        if(i.isalpha()):
            res=True
        else:
            raise NameError

try:
    print("="*70)
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    while(True):
        id=int(input("Enter Id :"))
        name=Namechk(input("Enter name :"))
        salary=float(input("Enter salary :"))
        cname=input("Enter c name :")
        desg=input("Enter desgnation")
        qry="insert into emp values(%d,'%s',%f,'%s','%s')"
        cur.execute(qry %(id,name,salary,cname,desg))
        print("data saved in emp table ")
        con.commit()
        #con.close()
        ask=input("add new row yes/no :")
        if(ask=="no"):
            break

except orc.DatabaseError as db:
    print("problem in database ",db)
except ValueError:
    print("ont Enter alphanumeri in place id/Salary")

except NameError:
    print("dont enter number or alphanum value in place of name")