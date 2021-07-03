from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.attributes("-fullscreen", True)
# background display
bg = PhotoImage(file="D:\\Project\\1.png")
bglab = Label(root, image=bg, bg="#5cc2d6")
bglab.place(x=0, y=0, relwidth=1, relheight=1)

# Add image file
root.title("CS Project 2021")
# Finding cgpa and displaying output
l1 = Label(root, text="Final Grade and Placement", font="Impact 33", bg="#373737", fg="white")
l1.pack(pady=20)

# isa 1 marks
isa1 = Label(root, text="Enter ISA-1 marks(average out of 60)", bg="#373737", fg="blanchedalmond", font="Arial 20")
isa1.pack(pady=20)
e1 = Entry(root, bg="#CCFF00", fg="black",borderwidth=5,highlightbackground="black",highlightthickness=4)
e1.pack()

# isa 2 marks
isa2 = Label(root, text="Enter ISA-2 marks(average out of 40)", bg="#373737", fg="blanchedalmond", font="Arial 20")
isa2.pack(pady=20)
e2 = Entry(root, bg="#FFFF66", fg="black",borderwidth=5,highlightbackground="black",highlightthickness=4)
e2.pack()

# esa marks
esa = Label(root, text="Enter ESA marks(average out of 100)", bg="#373737", fg="blanchedalmond", font="Arial 20")
esa.pack(pady=20)
e3 = Entry(root, bg="#FFA6C9", fg="black",borderwidth=5,highlightbackground="black",highlightthickness=4)
e3.pack()
# Assignment marks
assignment = Label(root, text="Enter assignment marks(average out of 10)", bg="#373737", fg="blanchedalmond",font="Arial 20")
assignment.pack(pady=20)
e4 = Entry(root, bg="#AAF0D1", fg="black",borderwidth=5,highlightbackground="black",highlightthickness=4)
e4.pack(pady=10)

check = 0
flag = 0


# function that calculates the cgpa
def final():
    global check
    global flag
    if check == 0:
        # isa1 marks =is1m
        is1m = e1.get()
        if not is1m.isdigit() or eval(is1m) > 60:
            mb.showerror("Error", "Please enter valid input for ISA-1 marks")
            flag = 1
        else:
            flag = 0
            # final marks =fm1
            fm1 = (int(is1m) / 60) * 24
        # isa2 marks =is2m
        is2m = e2.get()
        if not is2m.isdigit() or eval(is2m) > 40:
            mb.showerror("Error", "Please enter valid input for ISA-2 marks")
            flag = 1
        else:
            flag = 0
            # final marks =fm2
            fm2 = (int(is2m) / 40) * 16

        # esa marks=esam
        esam = e3.get()
        if not esam.isdigit() or eval(esam) > 100:
            mb.showerror("Error", "Please enter valid input for ESA marks")
            flag = 1
        else:
            flag = 0
            fe = int(esam) / 2
        # assignment marks
        assign = e4.get()
        if not assign.isdigit() or eval(assign) > 10:
            mb.showerror("Error", "Please enter valid input for assignment marks")
            flag = 1
        else:
            flag = 0
            assign = int(assign)

        p = (fm1 + fm2 + fe + assign)
        cgpa = p / 9.5
        cgpa = round(cgpa, 2)

        # calculating tier
        if cgpa > 9:
            company = "Tier 1 company."

        elif cgpa > 8:
            company = "Tier 2 company."

        elif cgpa > 7:
            company = "Tier 3 company"
        elif cgpa > 5:
            company = "Low Tier company"
        else:
            company = "Minimum CGPA of 5 is required for placement"

        c.config(text="CGPA is : " + str(cgpa), font=" fixedsys 25", bg="#373737", fg="white")
        tier.config(text="" + company, font="fixedsys 25", bg="#373737", fg="white")
        check = 1


# placement display
pb = Button(root, text="Click here for placement information", font="verdana 20", bg="grey",fg="black",borderwidth=7,command=final)
pb.pack(pady=10)

if flag == 0:
    c = Label(root, bg="#282829")
    tier = Label(root, bg="#282828")
    c.pack()
    tier.pack()
    flag = 1

# submit values and displaying courses
course = ""
l4 = Label(root, font="fixedsys 24", text=course, bg="#373737", fg="white")


def submit(lb):
    global course
    info = str(lb.get(lb.curselection()))
    if info == "Accounts and Finance":
        course = "Bcom Honours \n Bcom Accounting and finance \n Bcom tourism"
    elif info == "Artificial intelligence":
        course = "Machine Learning \n  Bachelor of Data Science \n AI and data science"
    elif info == "Coding":
        course = "PG Program in Big Data Engineering \n Master of Science in Data Science \n Software Engineering \n "
    elif info == "Design":
        course = "BFA Fashion Design \n Diploma in Fashion Design & Merchandising \n UX/UI Designing\n 3-D Graphics and Designing"
    elif info == "Gaming":
        course = "Diploma in Production Gaming\n Diploma in Game Design and Integration"
    elif info == "Humanities and political science":
        course = "BA Political Science\n  BA History \n Philosophy and critical thinking\n"
    elif info == "Instrumental Music":
        course = "BA Music\n BFA Music \n Introduction to music theory \n Music technology and foundations"
    elif info == "Law":
        course = "BA LLB \n Diploma in Corporate Laws & Management \n Psychology of criminal justice \n Comparitive judicial systems"
    elif info == "Marketing or Business":
        course = "MBA \n  Marketing Strategy and Management \n"
    elif info == "Photography":
        course = "PG Diploma in Photography \n Diploma in Professional Photojournalism"
    elif info == "Science and technology":
        course = "Big Data Engineer Master's Program\n Aeronautical Engineering\n Mechatronics Engineering"
    elif info == "Medicine":
        course="Principles of Biochemistry\nMbbs( Medicinae Baccalaureus Baccalaureus Chirurgiae) \nDrug discovery and medicinal chemistry\nMental health and Nurition"
    elif info == "Space and astronomy":
        course = "MSc in astronomy\n B.Tech in Aerospace Engineering\nMSc in astrophysics. "
    elif info == "Sports and yoga":
        course = "Diploma in Sports Management\n Diploma in Sports Science & Nutrition"
    else:
        course = "Please choose a field of interest"
    # courses display label
    l4.config(text=course)
    l4.pack()


# clearing window and displaying a new window
def courses():
    list_pack = root.pack_slaves()
    for i in list_pack:
        i.pack_forget()
    # suggesting courses based on interests
    l2 = Label(root, text="Suggested Courses", font="Impact 33", bg="#373737", fg="white")
    l2.pack(pady=16)
    l3 = Label(root, text="Choose your interest", font="Sans-Seriff 24", bg="#373737", fg="blanchedalmond")
    l3.pack(pady=15)
    # SECOND WINDOW(COURSES)
    lb = Listbox(root, font="Arial", cursor="cross",bg="#aef571",height=14, width=25)
    lb.insert(1, "Accounts and Finance")
    lb.insert(2, "Artificial intelligence")
    lb.insert(3, "Coding")
    lb.insert(4, "Design")
    lb.insert(5, "Gaming")
    lb.insert(6, "Humanities and political science")
    lb.insert(7, "Instrumental Music")
    lb.insert(8, "Law")
    lb.insert(9, "Marketing or Business")
    lb.insert(10,"Medicine")
    lb.insert(11, "Photography")
    lb.insert(12, "Science and technology")
    lb.insert(13, "Space and astronomy")
    lb.insert(14, "Sports and yoga")
    lb.pack(pady=10)
    # submit button
    sb = Button(root, text="Submit", font="verdana 15", bg="grey", fg="black",borderwidth=7,command=lambda: submit(lb))
    sb.pack(pady=10)
    ex = Button(root, text="Exit", font="verdana 15", bg="grey", fg="black",borderwidth=7, command=lambda: root.destroy())
    ex.pack(pady=10)


# courses button
cb = Button(root, text="Click here for suggested courses", font="verdana 20", bg="grey", fg="black",borderwidth=7, command=courses)
cb.pack(pady=10)



root.mainloop()
