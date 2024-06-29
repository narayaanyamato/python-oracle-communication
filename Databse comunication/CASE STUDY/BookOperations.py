
def Addbook():
    import oracledb as orc
    print("*"*70)
    try:
        con=orc.connect("system/narayan@localhost/XE")
        cur=con.cursor()
        while(True):
            bid = int(input("Enter book id:"))
            bname = input("Enter book name:")
            bprice = float(input("Enter book price:"))
            bautho = input("Enter book author:")
            qry = "insert into books values(%d,'%s',%f,'%s')"
            cur.execute(qry % (bid, bname, bprice, bautho))
            print("Book  saved ")
            con.commit()
            print("-->"*70)
            y=input("Add new record (yes/No):").lower()
            if(y=="no"):
                break;



    except orc.DatabaseError as db:
        print("\u001b[31;1m"+"Error in :",db)
    except ValueError:
        print("\u001b[31;1m"+"wrong value input in place of number field ")


def Removebook():
    import oracledb as orc
    print("*" * 70)
    try:
        con = orc.connect("system/narayan@localhost/XE")
        cur = con.cursor()
        bid = int(input("Enter book id :"))
        qry = "delete from books where bid=%d"
        cur.execute(qry %bid)
        print("\u001b[33;1m"+"book removed ")
        con.commit()
        con.close()

    except orc.DatabaseError as db:
        print("\u001b[31;1m"+"Error in :", db)
    except ValueError:
        print("\u001b[31;1m"+"wrong value input in place of number field ")



def Updatebook():
    import oracledb as orc
    print("*" * 70)
    try:
        con = orc.connect("system/narayan@localhost/XE")
        cur = con.cursor()
        print("\u001b[33;1m"+"select column want to update :")
        print("\u001b[33;1m"+"a]price \t b]author\t c]book name")
        print("-"*50)
        c=input("Enter above alpha : ").lower()
        if(c=="a"):
            p=int(input("Enter price :"))
            bid = int(input("Enter book id :"))
            qry="update books set bprice=%d where bid=%d"
            cur.execute(qry %(p,bid))
            print("\u001b[33;1m"+"book updated")
            con.commit()
        elif(c=="b"):
            p = input("Enter Author name :")
            bid = int(input("Enter book id :"))
            qry = "update books set bauthor='%s' where bid=%d"
            cur.execute(qry % (p, bid))
            print("\u001b[33;1m"+"book updated")
            con.commit()
        elif(c=="c"):
            p = input("Enter book name :")
            bid = int(input("Enter book id :"))
            qry = "update books set bname='%s' where bid=%d"
            cur.execute(qry % (p, bid))
            print("\u001b[33;1m"+"book updated")
            con.commit()

        con.close()

    except orc.DatabaseError as db:
        print("\u001b[31;1m"+"Error in :", db)
    except ValueError:
        print("\u001b[31;1m"+"wrong value input in place of number field ")




def Viewbook():
    import oracledb as orc
    print("*" * 70)
    try:
        con = orc.connect("system/narayan@localhost/XE")
        cur = con.cursor()
        qry = "select * from books"
        cur.execute(qry)
        res=cur.fetchmany()
        for i in res:
            print(i,end="")
            print()


    except orc.DatabaseError as db:
        print("\u001b[31;1m"+"Error in :", db)
    except ValueError:
        print("\u001b[31;1m"+"wrong value input in place of number field ")

