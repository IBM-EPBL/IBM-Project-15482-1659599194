'''
in this package has two methods Fetchdata and adddata
Fetchdata ==> fetch the user information when logged in
adddata  ==> add user data into database
'''
from auth import LogAuth,db2 

def fetchData(userId):
    users_ref = db2.db.collection(u'users')
    docs = users_ref.stream()
    fetchData={}
    for doc in docs:
        if doc.id==userId:
            fetchData['id']=userId
            fetchData['name']=doc.to_dict()['name']
            fetchData['email']=doc.to_dict()['email']
            return fetchData

def addData(user,name,email):
    LogAuth.auth.send_email_verification(user)
    info = LogAuth.auth.get_account_info(user)
            # create table individual id,name,email
    data ={
                'id':info['users'][0]['localId'],
                'name':name,
                'email':email
            }
    db2.db.collection('users').document(info['users'][0]['localId']).set(data)
