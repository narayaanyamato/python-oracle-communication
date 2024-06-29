import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    cols=[]
    qry="select * from emp"
    cur.execute(qry)
    res=cur.description
    for i in res:
        cols.append(i[0])
    for j in cols:
        print(j,"\t")
    print("-"*70)
    rec=cur.fetchall()
    for rval in rec:
        print(rval)
except orc.DatabaseError as db:
    print("Error in:",db)