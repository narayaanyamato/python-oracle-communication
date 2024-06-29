import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    col=input("Enter colum name : ")
    col2=input("new column name :")
    cur.execute("alter table student rename column %s to %s"%(col,col2))
    print("column renamed")

except orc.DatabaseError as db:

    print("problem in",db)
    
