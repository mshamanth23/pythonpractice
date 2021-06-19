import sqlite3
class student:
    def __init__(self):
        self.conn=sqlite3.connect('test.db')
        cur=self.conn.cursor()
        cur.execute("""create table if not exists students(sname text(30),
        regno integer(20))""")
        cur.close()
    def add(self,regno,sname):
        try:
            cur=self.conn.cursor()
            cur.execute("insert into students values(?,?)",(sname,regno))
        except:
            self.conn.rollback()
            print("Error happened")
            return False
        else:
            self.conn.commit()
            print("1 row is created")
            return True
        finally:
            self.conn.close()
    def display(self,regno):
        try:
            cur=self.conn.cursor()
            cur.execute(f"select * from students where regno = {regno}")
            student = cur.fetchone()
            print(f"""sname:{student[0]}  regno:{student[1]}""")

        except:
            print("Error happened")
        else:
            print("records are shown")


        finally:
            self.conn.close()
    def displayall(self):
        try:
            cur = self.conn.cursor()
            cur.execute("select * from students order by regno")
            result=cur.fetchall()
            for i in result:
                print(f""" sname:{i[0]} regno:{i[1]}""")
        except:
            print("error")
        else:
            print("records are shown")
        finally:
            self.conn.close()
    def update(self,regno,sname):
        try:
            cur = self.conn.cursor()
            cur.execute("update students set sname=? where regno=?",(sname,regno))
        except Exception as e:



            print(e)
            return False

        else:

            print("updated")
            return True

        finally:
            self.conn.close()
    def delet(self,regno):
        try:
            cur = self.conn.cursor()
            cur.execute(f"delete from students where regno = {regno}")
        except:
            self.conn.rollback()
            print("error")
        else:
            self.conn.commit()
            print("deleted")
        finally:
            self.conn.close()
