from flask import *
from db import todolist,addTask,update,submitted_task_list,deletetask

f=Flask(__name__)

@f.route('/')
def index():
    tlist=todolist()
    count=0
    count+=len(todolist())
    
    scount=0
    scount+=len(submitted_task_list())
    print(count,scount)
    return render_template("index.html",list=tlist,pcnt=count,scnt=scount,msg="Todo List")

@f.route('/pending')
def pending_task_list():
    tlist=todolist()
    count=0
    count+=len(todolist())
    
    scount=0
    scount+=len(submitted_task_list())
    print(count,scount)
    return render_template("index.html",list=tlist,msg="Todo List",pcnt=count,scnt=scount)

@f.route('/addtask',methods=['GET','POST'])
def add_task():
    if request.method=='POST':
        task_title=request.form['title']
        task_description=request.form['description']
        doc=request.form['doc']
        t=(task_title,task_description,doc)
        addTask(t)
        return redirect('/addtask')
    else:
        return render_template("addtask.html")

@f.route('/completed')
def update_list():
    id=request.args.get('id')
    update(id)
    return redirect('/pending')

@f.route('/submitted')
def submitted_task():
    st=submitted_task_list()
    count=0
    count+=len(todolist())
    
    scount=0
    scount+=len(submitted_task_list())
    print(count,scount)
    return render_template("index.html",slist=st,smsg="Tasks Marked as Completed",pcnt=count,scnt=scount)

@f.route('/delete')
def delete_task():
    id=request.args.get('id')
    deletetask(id)
    return redirect('/pending')

@f.route('/deletetask')
def delete_completed_task():
    id=request.args.get('id')
    deletetask(id)
    return redirect('/submitted')



if __name__=='__main__':
    f.run(debug=True)
   
