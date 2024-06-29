import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    qry="select * from emp"
    cur.execute(qry)
    colinfo=cur.description
    cilval=[]
    for i in colinfo:
        cilval.append(i[0])
    for j in cilval:
        print(j,end=" ")
except  orc.DatabaseError as db:
    print(db)


