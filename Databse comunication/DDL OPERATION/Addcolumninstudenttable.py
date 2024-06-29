import oracledb as orc
try:
    print(".."*70)
    conn=orc.connect("system/narayan@localhost/XE")
    cur=conn.cursor()
    col=input("Enter col name want to add in table :")
    cur.execute("alter table student add %s varchar(24)"%col)
    print("the column {} add in student table".format(col))
    print(".."*70)
except orc.DatabaseError as db:
    print("problem in",db)

