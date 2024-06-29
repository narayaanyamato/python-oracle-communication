import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    n=input("Enter name to Drop table ")
    cur.execute("drop table %s"%n)
    print("table removed")
except orc.DatabaseError as db:
    print("problem in query or database :",db)
