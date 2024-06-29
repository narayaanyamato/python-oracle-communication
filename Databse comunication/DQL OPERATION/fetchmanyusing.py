import oracledb as orc
try:
    con=orc.connect("system/narayan@127.0.0.1/XE")
    cur=con.cursor()
    qry="select * from emp"
    cur.execute(qry)
    res=cur.fetchmany()
    for i in res[::-1][1:5]:
        print(i)
except orc.DatabaseError as db:
    print("Error in :",db)