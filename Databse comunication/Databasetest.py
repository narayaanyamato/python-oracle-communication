import oracledb as orc
#print(orc.__version__)
#selrct * fromnglobal_name
#write a python python which demonstrate obtain connection from pracale datanase
try:
    conn=orc.connect("system/narayan@localhost/XE")
    print(conn)

except orc.DatabaseError as db:
    print("invalid username/password; logon denied")


    #write a python program whichwill chsnge size of table and table(change college )
    #write a python program whichwill reove a program which will fromoracleora