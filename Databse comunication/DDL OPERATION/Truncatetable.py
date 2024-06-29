import  oracledb as orc
try:
    print("*"*60)
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    n=input("Enter table name :")
    cur.execute("truncate table %s"%n)
    print("table truncated")
except orc.DatabaseError as db:
    print("problem in query",db)
