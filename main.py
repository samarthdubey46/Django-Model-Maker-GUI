import tkinter
root = tkinter.Tk()

def command(row1):
    s = list1[row1]["blank"]
    list1[row1]["blank"] = True if s is False else False


list1 = [
    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
        {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
            {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
                {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
                    {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},
                        {"id": '', "name": tkinter.StringVar(root), "typo": '', "main_name": 'is_active', "blank": tkinter.IntVar(
    ), "blankname": '', "typename": '', "fieldname": tkinter.StringVar(root), "comment": tkinter.StringVar(root), 'commentType': '',"ca":'',"ForiegnStr":tkinter.StringVar(root),"Foriegnobj":''},

]

row = 1
options = ("CharField")
class_n = tkinter.StringVar()
l9 = tkinter.Label(root, text="").grid(row=0, column=0, pady=2)
# l12 = tkinter.Label(root,text = "").grid(row=1,column=0,pady = 2)
class_n.set("name")
for i in list1:
    i['id'] = tkinter.Entry(root, textvariable=i["name"])
    i['Foriegnobj'] = tkinter.Entry(root, textvariable=i["ForiegnStr"])
    i['commentType'] = tkinter.Entry(root, textvariable=i["comment"])
    i["blank"].set(0)
    i['typo'] = tkinter.OptionMenu(root, i["fieldname"], options, "BooleanField", "IntegerField", "DateTimeField", "EmailField", "ImageField",
                                   "UUIDField", "URLField", "DecimalField","ForeignKey")
    i['blankname'] = tkinter.Checkbutton(
        root, variable=i["blank"], onvalue=1, offvalue=0)
    l1 = tkinter.Label(root, text="Name").grid(
        row=row, column=0, pady=2, padx=5)
    l2 = tkinter.Label(root, text="Type").grid(
        row=row, column=2, pady=2, padx=5)
    l3 = tkinter.Label(root, text="Black").grid(
        row=row, column=4, pady=2, padx=5)
    l4 = tkinter.Label(root, text="Comment").grid(
        row=row, column=8, pady=2, padx=5)
    l4 = tkinter.Label(root, text="ForiegnObject").grid(
        row=row, column=6, pady=2, padx=5)
    i['id'].grid(row=row, column=1, pady=4, padx=5)
    i['typo'].grid(row=row, column=3, pady=4, padx=5)
    i['blankname'].grid(row=row, column=5, padx=5)
    i['commentType'].grid(row=row, column=9, padx=5)
    i['Foriegnobj'].grid(row=row,column=7,padx=5)
    if(row > 2):
        i["fieldname"].set("CharField")
    row += 1
classs = tkinter.Entry(root, textvariable=class_n)
label = tkinter.Label(root, text="Class").place(x=250, y=5)
classs.place(x=300, y=5)

list1[0]["name"].set("is_active")
list1[1]["name"].set("create_update_at")
list1[0]["fieldname"].set("BooleanField")
list1[1]["fieldname"].set("DateTimeField")

def onpress():
    with open(str(class_n.get()) + '.py' if class_n.get() is not None else "name.py", 'a') as obj:
        obj.write("from django.db import models")
        obj.write('\n')
        obj.write("class {0}(models.Model):".format(class_n.get()))
        obj.write('\n')

    for i in list1:
        name = i.get("name").get()
        types = i.get("fieldname").get()
        comment = i.get("comment").get()
        foriegn_key = i.get("ForiegnStr").get()
        blank = "True" if i.get("blank").get() == 1 else "False"

        if(types == "CharField" or types == "EmailField" or types == "URLField"):
            string = f"{name} = models.{str(types)}(max_length=500,blank={blank}) // {comment}"
            if(name != ""):
                with open(str(class_n.get()) + '.py' if class_n.get() is not None else "name.py", 'a') as obj:
                    obj.write('\t' + string)
                    obj.write('\n')
        if(types == "ForeignKey"):
            print(types)
            string = f"{name} = models.{str(types)}({foriegn_key},on_delete=models.CASCADE) // {comment}"
            if(name != ""):
                with open(str(class_n.get()) + '.py' if class_n.get() is not None else "name.py", 'a') as obj:
                    obj.write('\t' + string)
                    obj.write('\n')
        if(types=="BooleanField"):
            string = f"{name} = models.{str(types)}(default=False,blank={blank}) // {comment}"
            if(name != ""):
                with open(str(class_n.get()) + '.py' if class_n.get() is not None else "name.py", 'a') as obj:
                    obj.write('\t' + string)
                    obj.write('\n')
        if(types == "DecimalField"):
            string = f"{name} = models.{str(types)}(max_digits=500,decimal_places=2,blank={blank}) // {comment}"
            if(name != ""):
                with open(str(class_n.get()) + '.py' if class_n.get() is not None else "name.py", 'a') as obj:
                    obj.write('\t' + string)
                    obj.write('\n')

        if(types == "IntegerField" or types == "DateTimeField" or types == "ImageField" or types == "UUIDField") :
            string = f"{name} = models.{str(types)}(blank={blank}) // {comment}"
            if(name != ""):
                with open(str(class_n.get()) + '.py' if class_n.get() is not None else "name.py", 'a') as obj:
                    obj.write('\t' + string)
                    obj.write('\n')


tkinter.Button(root, text="Sumbit", command=onpress).grid(row=row+1, column=5,pady=14)
root.mainloop()
