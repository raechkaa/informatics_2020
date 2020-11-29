class Terminate(Exception):
   pass

class Connection(Exception):
    pass

def write_to_file(f_obj):
    while True:
        try:
            x = yield
            f_obj.write(x + '\n')
        except Terminate:
            break

def connect_user(logins):
    with open('message.txt','w') as file:
        yield from write_to_file(file)

def user_connection(logins):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{logins} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"

def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]

def task_planner():
    x = 0
    #print('zdes rabotaet')
    while True:
        try:
            x = yield from connect_user(x)
            #print(x)
            connect_user(x)
        except Connection:
            break

coroutine = task_planner()
next(coroutine)
for i in establish_connection(): 
    coroutine.send(i)

for i in establish_connection(False): 
    pass #потому что неавторизованных не записываем в файл

