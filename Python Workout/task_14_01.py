users = {
    'user1': 'passwd1',
    'user2': 'passwd2',
    'user3': 'passwd3',
    'user4': 'passwd4',
    'user5': 'passwd5',
}

def login():
    user = input('Login: ')
    if user in users:
        pwd = input('Password: ')
        if pwd == users[user]:
            print('Access granted!')
        else:
            print('Access denied!')
    else:
        print('Access denied!')

login()
