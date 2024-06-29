import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    #id=int(input("Enter id :"))
    n=str(input("Enter name :"))
    s=int(input("Enter salary :"))
    cur.execute("update emp set salary =%d where name='%s' " %(s,n))
    print("data is updated !")
    con.commit()
    con.close()
except orc.DatabaseError as db:
    print("problem in database",db)
except ValueError:
    print("dont num place alphanumic and alpha numic place num")

