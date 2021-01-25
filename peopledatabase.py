from tkinter import *

master = Tk()
master.configure(background='black')

master.title("Database Login")
Label(master, text="User Name",background='black',fg='white').grid(row=0)
Label(master, text="Password",bg='black',fg='white').grid(row=1)
def entryreturn(en):
    text=e1.get()
    text1=e2.get()
    if text=="username":
        if text1=="password":
            wind = Tk()
            wind.title("Classified")
            wind.grid()
            T = Text(wind, height=2, width=30)
            T.pack()
            import re
            shakes = open("femalenames.txt", "r")
            s3=0
            y3=2
            def search():
                def form1(en):
                    input1=e3.get()
                    count=0
                    s=0
                    y=2
                    while s!=y:
                        for line in shakes:
                            if re.match(input1, line):
                                a=count
                                with open("femalenumbers.txt", "r") as f:
                                    for x, line in enumerate(f):
                                        if x==a:
                                            T.insert(END, line)
                                            with open("countries.txt", "r") as c:
                                                for x, line in enumerate(c):
                                                    if x==a:
                                                            
                                                        T.insert(END, line)
                                                                                                                                                           
                                            return
                            else:
                                count +=1
                Label(master, text="Name", fg='white', bg='black').grid(row=3)
                e3=Entry(master)
                e3.grid(row=3, column=1)
                e3.bind('<Return>',form1)
            shake = open("malenames.txt", "r")
            def search2():
                def form2(en):
                    input2=e4.get()
                    count1=0
                    s1=0
                    y1=2
                    while s1!=y1:
                        for line in shake:
                            if re.match(input2, line):
                                a=count1
                                with open("malenumbers.txt", "r") as b:
                                    for x, line in enumerate(b):
                                        if x==a:
                                                
                                            T.insert(END, line)
                                                
                                            with open("countries.txt", "r") as c:
                                                for x, line in enumerate(c):
                                                    if x==a:
                                                            
                                                        T.insert(END, line)
                                                            
                                            return
                            else:
                                count1 +=1
                Label(master, text="Name", fg='white', bg='black').grid(row=3)
                e4=Entry(master)
                e4.grid(row=3, column=1)
                e4.bind('<Return>',form2)
            def maleorfemale(en):
                ask=e6.get()
                if ask=="male" or "Male":
                    search2()
                elif ask=="female" or "Female":
                    search()
            Label(master, text="Male or Female",fg='white',bg='black').grid(row=2)
            e6=Entry(master)
            e6.grid(row=2, column=1)
            e6.bind('<Return>', maleorfemale)
            wind.mainloop()

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

e1.bind('<Return>', entryreturn) 
e2.bind('<Return>', entryreturn) 

mainloop()

