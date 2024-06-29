#write a python program which will accept key from keyword and insert in emp table
import oracledb as orc
try:
    print("=" * 70)
    conn=orc.connect("system/narayan@localhost/XE")
    cur=conn.cursor()
    sql="insert into emp values(1,'narayan',19000,'wipro','trainee')"
    cur.execute(sql)
    conn.commit()
    print("="*70)
    print("data saved in emp table")

except orc.DatabaseError as db:

    print("problem in ",db)

