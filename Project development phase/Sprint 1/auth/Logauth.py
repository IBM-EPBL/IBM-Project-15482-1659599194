'''
These file load credentials of authenication system
The sensitive information keys are removed
'''
import pyrebase
config ={
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "databaseURL":""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
