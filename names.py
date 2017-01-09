users = {
 'Students': [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for group in users:
    print "\n",group
    count = 1
    for name in users[group]:
        print str(count), "-" , name['first_name'], name['last_name'], "-", str(len(name['first_name'])+len(name['last_name']))
        count += 1
