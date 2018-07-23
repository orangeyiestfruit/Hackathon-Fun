import sqlite3
conn = sqlite3.connect('thelogin.db')
c = conn.cursor()

def create_table(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+"(user TEXT,password TEXT)")
def create_table2(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+" (user TEXT, appliance, TEXT)")
create_table("login")
create_table2("appliances")    
def data_entry_login(username,password):
    c.execute("INSERT INTO login (user,password) VALUES(?,?)",(username,password))
    conn.commit()
def data_entry_appliances(owner,appliancename):
    c.execute("INSERT INTO login (user,appliance) VALUES(?,?)",(owner,appliancename))
    conn.commit()
#data_entry_login("Edwin0101","Pawn1234")
def login_password(username):
    c.execute("SELECT password FROM login WHERE user='"+username+"'")
    for row in c.fetchall():
        return row[0]
def appliance_appliances(username):
    c.execute("SELECT appliance from appliances WHERE user='"+username+"'")
    for row in c.fetchall():
        return row[0]
