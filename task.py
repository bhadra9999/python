nodes = []
print("Enter 10 node names")
for i in range(3):
    instance = str(input("Enter the server "))
    nodes.append(instance)


#print the list
for i in nodes:
    env = i[:3]
# print env
if i.startswith('dev'):
    length = len(i)
    i = i.capitalize()
    print("%s is %s environemnt and the length is %d" % (i,env,length))
if i.startswith('uat'):
    length = len(i)
    i = i.capitalize()
    print("%s is %s enviroment and the length is %d" % (i,env,length))
if i.startswith('prd'):
    length = len(i)
    i = i.capitalize()
    print("%s is %s enviroment and the length is %d" % (i,env,length))