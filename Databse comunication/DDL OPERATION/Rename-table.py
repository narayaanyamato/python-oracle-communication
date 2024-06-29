import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    n=input("Enter new tablename :")

    cur.execute("alter table std rename to %s "%n)
    print("table renamed")
except orc.DatabaseError as db:
    print("problem in query or database :",db)