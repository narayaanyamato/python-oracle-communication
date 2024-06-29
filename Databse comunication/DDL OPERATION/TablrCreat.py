import oracledb as orc
try:
    print("=+"*60)
    conn=orc.connect("system/narayan@localhost/XE")
    cur=conn.cursor()
    sql="create table student(std_id number(3),std_name varchar(20),std_rolno number(10),std_course varchar(10))"
    cur.execute(sql)
    print("table created")
except orc.DatabaseError as db:
    print("print Error in data base",db)