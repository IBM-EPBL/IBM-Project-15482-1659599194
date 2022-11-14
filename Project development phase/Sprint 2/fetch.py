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
            fetchData['number']=doc.to_dict()['number']
            fetchData['jobFetchCount']=doc.to_dict()['jobFetchCount']
            fetchData['role']=doc.to_dict()['role']
            fetchData['skill1']=doc.to_dict()['skill1']
            fetchData['skill2']=doc.to_dict()['skill2']
            fetchData['skill3']=doc.to_dict()['skill3']
            fetchData['update']=doc.to_dict()['update']
            return fetchData

def addData(user,name,email):
    info = LogAuth.auth.get_account_info(user)
            # create table individual id,name,email
    data ={
                'id':info['users'][0]['localId'],
                'name':name,
                'email':email,
                'number':'',
                'role':'',
                'skill1':'',
                'skill2':'',
                'skill3':'',
                'update':False,
                'jobFetchCount':0
            }
    db2.db.collection('users').document(info['users'][0]['localId']).set(data)


