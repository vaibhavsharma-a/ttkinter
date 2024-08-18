from tkinter import *
import sqlite3


root = Tk()
root.title("Creating database")
root.geometry("300x450")

#creating or connecting the database

conn = sqlite3.connect("Cricket_records.db")
#creating a cursor

c = conn.cursor()


# c.execute("""
#           CREATE TABLE Players(
#           Name text,
#           Age integer,
#           Nation text,
#           Matches integer,
#           Scores integer

#           )""")

#? To check if the table exist in the database once we have run the command of creating a table
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")

# # Fetch all results from the executed query
# tables = c.fetchall()

# # Print the list of tables
# for table in tables:
#     print(table[0])

def submit():
  #clear the text boxes
  conn = sqlite3.connect("Cricket_records.db")

  c = conn.cursor()

  c.execute("INSERT INTO Players VALUES(:Name, :Age, :Nation, :Matches, :Scores)",
            {
              'Name' : Name.get(),
              'Age' : Age.get(),
              'Nation' : Nation.get(),
              'Matches' : Matches.get(),
              'Scores' : Scores.get()
            })




  conn.commit()

  conn.close()


  Name.delete(0,END)
  Age.delete(0,END)
  Nation.delete(0,END)
  Matches.delete(0,END)
  Scores.delete(0,END)

def query():
  conn = sqlite3.connect("Cricket_records.db")

  c = conn.cursor()

  c.execute("SELECT *, oid FROM Players")
  recor = c.fetchall()
  print(recor)

  print_record = ""
  
  for records in recor:
    print_record += "Name" + " " + str(records[0]) + " " +"OID" + " " + str(records[5]) + "\n"
    

  qurey_lable = Label(root,text=print_record)
  qurey_lable.grid(row=10,column=1,columnspan=2)




  conn.commit()
  conn.close()

#! to delete a record

def delt():
  conn = sqlite3.connect("Cricket_records.db")

  c = conn.cursor()

  c.execute("DELETE From Players WHERE oid = " + delete_box.get())

  delete_box.delete(0,END)






  conn.commit()
  conn.close()

def update():
  pass
#! to edit 

def edit():
  
  editor = Tk()
  editor.title("Edit your records")
  editor.geometry("300x450")

  conn = sqlite3.connect("Cricket_records.db")

  c = conn.cursor()

  rec = delete_box.get()
  c.execute("SELECT * FROM Players WHERE oid =" + rec)
  recor = c.fetchall()
  
    

  Name_ed = Entry(editor,width=30)
  Name_ed.grid(row=0,column=1,pady=(10,0))

  Age_ed = Entry(editor,width=30)
  Age_ed.grid(row=1,column=1)

  Nation_ed = Entry(editor,width=30)
  Nation_ed.grid(row=2,column=1)

  Matches_ed = Entry(editor,width=30)
  Matches_ed.grid(row=3,column=1)

  Scores_ed = Entry(editor,width=30)
  Scores_ed.grid(row=4,column=1)



  Nam_ed = Label(editor,text="Name")
  Nam_ed.grid(row=0,column=0,pady=(10,0))

  Ag_ed = Label(editor,text="Age")
  Ag_ed.grid(row=1,column=0)

  Natio_ed = Label(editor,text="Nation")
  Natio_ed.grid(row=2,column=0)

  Matche_ed = Label(editor,text="Matches")
  Matche_ed.grid(row=3,column=0)

  Score_ed = Label(editor,text="Name")
  Score_ed.grid(row=4,column=0)

  for recs in recor:
    Name_ed.insert(0,recs[0])
    Age_ed.insert(0,recs[1])
    Nation_ed.insert(0,recs[2])
    Matches_ed.insert(0,recs[3])
    Scores_ed.insert(0,recs[4])


  edt_button = Button(editor,text="Save Edit",command=update)
  edt_button.grid(row=5,column=1,columnspan=2,padx=5,pady=5)


#? Making text boxes

Name = Entry(root,width=30)
Name.grid(row=0,column=1,pady=(10,0))

Age = Entry(root,width=30)
Age.grid(row=1,column=1)

Nation = Entry(root,width=30)
Nation.grid(row=2,column=1)

Matches = Entry(root,width=30)
Matches.grid(row=3,column=1)

Scores = Entry(root,width=30)
Scores.grid(row=4,column=1)

delete_box = Entry(root,width=30)
delete_box.grid(row=7,column=1)

#creating lables for the text fields

Nam = Label(root,text="Name")
Nam.grid(row=0,column=0,pady=(10,0))

Ag = Label(root,text="Age")
Ag.grid(row=1,column=0)

Natio = Label(root,text="Nation")
Natio.grid(row=2,column=0)

Matche = Label(root,text="Matches")
Matche.grid(row=3,column=0)

Score = Label(root,text="Scores")
Score.grid(row=4,column=0)

delet = Label(root,text="Select ID")
delet.grid(row=7,column=0)

#! create a submit button

sbmit = Button(root,text="Submit the record",command=submit)
sbmit.grid(row=5,column=1,columnspan=2,padx=5,pady=5)
#commite the changes in db

#! query button to check for the values we have entered
qury = Button(root,text="Show records",command=query)
qury.grid(row=6,column=1,columnspan=2,padx=5,pady=5)


#! delete button
dlt_btn = Button(root,text="Delete the record",command=delt)
dlt_btn.grid(row=8,column=1,columnspan=2,padx=5,pady=5)

#! edit button
edt_button = Button(root,text="Edit record",command=edit)
edt_button.grid(row=9,column=1,columnspan=2,padx=5,pady=5)
conn.commit()





#close the database(expicitly)
conn.close()
root.mainloop()