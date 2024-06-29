import oracledb as orc
try:

    conn=orc.connect("system/narayan@localhost/XE")
    cur=conn.cursor()
    id=int(input("Enter id"))
    name=input("Enter name")
    salary=int(input("Enter salary"))
    cname=input("Enter company")
    desg=input("Enter desgination ")
    sql = "insert into emp values(:id, :name, :salary, :cname, :desg)"
    cur.execute(sql, {'id': id, 'name': name, 'salary': salary, 'cname': cname, 'desg': desg})
    conn.commit()
    
    print("data saved in table ")

except orc.DatabaseError as db:
    print("error in ",db)
except ValueError:
    print("enter valid input number place number and str place str")