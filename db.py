import pymysql as p


def connect():
    return p.connect(host='localhost',user='root',password='',database='pytodb')

def addTask(t):
    db=connect()
    cr=db.cursor()
    sql='insert into todo(task_title,task_description,doc) values(%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()

def todolist():
    db=connect()
    cr=db.cursor()
    sql='select * from todo where status=0'
    cr.execute(sql)
    ulist=cr.fetchall()
    db.commit()
    db.close()
    return ulist

def update(id):
    db=connect()
    cr=db.cursor()
    sql='update todo set status=1,doc=CURRENT_TIMESTAMP where id=%s'
    cr.execute(sql,id)
    db.commit()
    db.close()

def submitted_task_list():
    db=connect()
    cr=db.cursor()
    sql='select * from todo where status=1'
    cr.execute(sql)
    ulist=cr.fetchall()
    db.commit()
    db.close()
    return ulist

def deletetask(id):
    db=connect()
    cr=db.cursor()
    sql='delete from todo where id=%s'
    cr.execute(sql,id)
    db.commit()
    db.close()
