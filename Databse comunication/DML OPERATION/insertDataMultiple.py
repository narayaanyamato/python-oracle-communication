import oracledb as orc
try:
    con=orc.connect("system/narayan@localhost/XE")
    cur=con.cursor()
    while(True):
        id=int(input("Enter id :"))
        name=input("Enter name :")
        salary=int(input("Enter salary :"))
        cname=input("enter c name")
        desg=input("Enter desgination :")
        sql="insert into emp values(:id,:name,:salary,:cname,:desg)"
        cur.execute(sql,{'id':id,'name':name,'salary':salary,'cname':cname,'desg':desg})
        print("data saved")
        r=input("Add new  data yes/no : ").lower()
        if(r=="no"):
            break

except orc.DatabaseError as db:
    print("error in data base",db)