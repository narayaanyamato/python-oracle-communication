import oracledb as orc
try:
    print("*"*60)
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    while(True):
        cname=input("Enter your cname ")
        sal=int(input("input your salary:"))
        eid=int(input("Enter ur emp no:"))y
        uq="update emp set cname='%s',salary=%d where id=%d"
        cur.execute(uq %(cname,sal,eid))
        con.commit()
        if(cur.rowcount>0):
            print("{} record updated".format(cur.rowcount))
        else:
            print("record not exist")

        add=input("Enter yes to add or no to exist").lower()
        if(add=="no"):
            break

except orc.DatabaseError as db:
    print("Error in :",db)