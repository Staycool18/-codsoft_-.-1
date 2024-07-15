from tkinter import *
from tkinter import messagebox

root=Tk() 
root.geometry("780x650+250+50")
root.title("To-Do-List")
root.config(bg='#342532')
#root.resizable(width=False, height=False)

tasks=[]

def add_task():  
    task_string = my_entry.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Task Is Empty.')  
    else:    
       lb.insert(END, task_string)
    my_entry.delete(0, "end")

def delete_task():
    lb.delete(ANCHOR)
    
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        lb.delete(0, END)
   
def close():    
    print(tasks)   
    root.destroy()

frame_1=Frame(root, width=750, height=100, bg='#342532')
frame_1.grid(row=0, column=0, padx=1, pady=1)

name=Label(frame_1, text="Enter Your tasks", font="ariel 17 bold", bg='#342532', fg="light blue")
name.place(x=10, y=20)

my_entry = Entry(
    frame_1,
    font=('times', 24)
    )
    
my_entry.place(x=220, y=20)

button_frame = Frame(root, width=760, height=150, bg="light yellow")
button_frame.grid(row=1, column=0, padx=10, pady=10)

add_button=Button(
    button_frame,
    text="Add Task",
    bd=10,
    font=("times 14"),
    bg="#c5f776",
    padx=20,
    pady=10,
    command = add_task
    )
del_button = Button(  
       button_frame, 
       text="Delete Task",
       bd=10, 
       font=("times 14"),
        bg="#c5f776",
        padx=20,
        pady=10,
        command = delete_task 
    )  
del_all_button = Button(  
        button_frame,  
         text="Delete All Tasks", 
         bd=10,
        font=("times 14"),
        bg="#c5f776",
        padx=20,
        pady=10,
        command = delete_all_tasks  
    )
    
exit_button = Button(  
        button_frame,  
         text="Exit", 
         bd=10,
       font=("times 14"),
        bg="#c5f776",
        padx=20,
        pady=10,
        command = close  
    )    
add_button.place(x = 20, y = 40,)  
del_button.place(x = 200, y = 40)  
del_all_button.place(x = 400, y = 40)  
exit_button.place(x = 640, y = 40)  

frame = Frame(root, width=400, height=200, bg="orange")
frame.grid(row=2, column=0, padx=1, pady=1) 

lb = Listbox(
    frame,
    width=50,
    height=13,
    font=('Times', 18),
    relief="solid",
    bg="light blue",
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"
)
lb.pack(side=LEFT, fill=BOTH)
    
root.mainloop()