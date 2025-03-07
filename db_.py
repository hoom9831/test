import sqlite3
class functions:
    def __init__(self,db):
        self.con=sqlite3.Connection('D:/hossien/my  H O O M/_ui_/person.db')
        self.cur=self.con.cursor()
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS  someone 
                        (id INTEGER PRIMARY KEY,fname text, lname text,term text,password text)
                        ''')
        self.con.commit()
        

    def insert_(self,fname,lname,term,password):
        self.cur.execute('INSERT INTO someone (fname , lname ,term,password) VALUES (?,?,?,?)',(fname,lname,term,password))
        self.con.commit()
 
    def show_(self):
        self.cur.execute('SELECT * FROM someone ')
        return self.cur.fetchall()

    def delet_(self,id,fname,lname,term,password):
        self.cur.execute('DELETE FROM someone WHERE id=? or fname=? or lname=? or term=? or password=?',(id,fname,lname,term,password))
        self.con.commit()

    def update_(self,id,fname,lname,term,password):
        self.cur.execute('UPDATE someone SET fname=? , lname=? , term=? , password=? WHERE id=?',(fname,lname,term,password,id))
        self.con.commit()

    def serch(self,password):
        self.cur.execute('select * from someone where password=?',(password,))
        return self.cur.fetchall()