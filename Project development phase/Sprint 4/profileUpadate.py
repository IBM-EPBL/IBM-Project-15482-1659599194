from auth import db2 

def update(userId,data):
    dataAdd = db2.db.collection(u'users').document(userId)
    dataAdd.update(data)


