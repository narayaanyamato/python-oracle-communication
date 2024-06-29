import oracledb as orc
try:
    con=orc.connect("system/narayan@127.0.0.1/XE")
    cur=con.cursor()
    qry="select * from emp"
    cur.execute(qry)
    while(True):
        res=cur.fetchone()
        if(res==None):
            break
        else:
          print(res,type(res))
except orc.DatabaseError as db:
    print("Error in :",db)