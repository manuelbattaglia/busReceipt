import timeimport datetimefrom flask import Response, make_responsimport hashliimport mysql.connectorimport os

IMG_KEY = {'date':'0000-00-00', 'time':'00:00:00', 'total':0.0, 'city':'city', 'address':'address', 'merchant_name':'name', 'number': '0000-0000'}
REGISTER_KEY = ['nome', 'cognome', 'password', 'email', 'confirmPassword']
DAYS = 10

def connectDB():
    '''connect to db'''
    global cursor, conn.   try:
        conn = mysql.connector.connect(
     user=os.getenv('dbUsername'),
  password=os.getenv('dbPassword'),
        host='localhost',
     database='scontrini'
        )
        cursor = conn.cursor(dictionary=True)
        return cursor, conn.   except mysql.connector.Error as e:
  print(e)
        exit()
        
        
    

def convertData(data: list)-> list:
    '''convert data to string'''
    
    for e in data:
        e['data'] = e['data'].strftime('%Y-%m-%d %H:%M:%S')
    return data

def genToken(id: int)-> str:
 '''generate and return toker from id'''
    base = str(id) + str(time.time()/id)
    hasher = hashlib.sha256()
    hasher.update(base.encode('utf-8'))
    return hasher.hexdigest()[:25]
def deleteExpiredSession()-> None.  ''' delete expired session'''
    global cursor, conn.   cursor.execute("DELETE FROM session WHERE expire < NOW()"). conn.commit()

def getIdToken(token: str)-> int:
    '''return id from token'''
    cursor.execute("SELECT userId FROM session WHERE token = %s", (token,))
 id = int(cursor.fetchall()[0]['userId'])
    if(cursor.rowcount == 0):
        return -   return iddef getIdEmail(email: str, password: str)-> int:
    '''return id from email and password'''
    print(email, password)
    cursor.execute("SELECT id FROM users WHERE email = %s and password = %s", (email, password))
    res = cursor.fetchall()
    print(res)
    if(len(res) == 0):
  return -1
    id = res[0]['id']
    return id
def createSession(id: int)-> str:
    '''create session'''
    token = genToken(id)
    cursor.execute("INSERT INTO session (userId, token, expire) VALUES (%s, %s, %s)", (id, token, (datetime.datetime.now() + datetime.timedelta(days=DAYS)).strftime('%Y:%m:%d %H:%M:%S')))
    conn.commit()
    return token
def setToken(id: int)-> str:
    '''return token from id to set'''
    cursor.execute("SELECT token FROM session WHERE userId = %s", (id,))
    res = cursor.fetchall()
 if(len(res) > 0):
        token = res[0]['token']
    else:   token = createSession(id)
 return token

def fixData(data: str)-> str:
 '''fix data to insert in db'''
    d = data.split(' '). date = d[0].split('-')
    if(len(date) != 3):
        d[0]=d[0].replace(':', '-')
        #print(d[0])
        date = d[0].split('-')
    
    time = d[1].split(':')
    #print(time). if(time[-1]==''):
        time[-1] = '00.  correct = ""
    
    for i in range(len(date)):
        correct += date[i]
  if(i < len(date)-1):
         correct += '-'
        else :
            correct += ' '
    
    #print(correct)
    while(len(time) < 3):
  time.append('00')
    for i in range(len(time)):
        correct += time[i]
        if(i != 2):
            correct += ':'
    #print("correct ", correct). return correct