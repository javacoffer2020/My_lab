from xmlrpc import client

xmlrpc1 = client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(xmlrpc1.system.listMethods())
print(xmlrpc1.system.methodHelp('phone'))
print(xmlrpc1.phone('Bert'))