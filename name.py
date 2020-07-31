#Not
import os

dirname = os.getcwd()
for i in os.listdir(dirname):
    if i.endswith('.py'):
            if(str(i) != "name.py"):
                he = []
                with open(os.path.join(dirname,i),'r') as files:
                        print(i)
                        listts = files.readlines()
                        for j,i in enumerate(listts):
                            if str(i[0:5]).strip() == "class":
                                print("Os")
                                print(j)
                                he.append(j)
                        print(he)
                        with open(os.path.join(dirname,'m/views.py'),'a') as obj:
                            print(listts[he[-1]:])
                            obj.writelines(listts[he[2]:])
                        # with open(os.path.join(dirname,'m/serelizers.py'),'a') as obj:
                        #     print(listts[he[1]:he[2]])
                        #     obj.writelines(listts[he[1]:he[2]])
                        # with open(os.path.join(dirname,'m/models.py'),'a') as obj:
                        #     print(listts[he[0]:he[1]])
                        #     obj.writelines(listts[he[0]:he[1]])

