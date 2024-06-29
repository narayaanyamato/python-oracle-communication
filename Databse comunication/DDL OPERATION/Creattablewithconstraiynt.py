import oracledb as orc
try:
    print("="*60)
    conn=orc.connect("system/narayan@127.0.0.1/XE")
    cur=conn.cursor()
    cur.execute("CREATE TABLE prod0ucts (product_id NUMBER(10), product_name VARCHAR2(50),product_description VARCHAR2(200),price NUMBER(30))")
    print("table created")
except orc.DatabaseError as db:
    print("Error in data ",db)