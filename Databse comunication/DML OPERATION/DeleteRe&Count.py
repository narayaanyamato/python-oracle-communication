import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    n=int(input("Enter id no: "))
    sql="delete from emp where id=%d "
    cur.execute(sql %n)
    con.commit()
    print("deleted record")

except orc.DatabaseError as db:
    print("Error in Database")
except ValueError:
    print("Enteron onlu num data")
