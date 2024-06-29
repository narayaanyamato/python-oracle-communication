import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    col=input("Enter colum name : ")
    cur.execute("alter table student drop column %s "%col)
    print("column Droped")

except orc.DatabaseError as db:

    print("problem in",db)