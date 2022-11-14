import json 
import requests
url = ""
headers = {
    "X-RapidAPI-Key": "",  
	"X-RapidAPI-Host": "pidapi.com"
}

from auth import db2 

def jobapi(id,count,role ="full stack developer",city ="chennai",country="india",pg='1'):
    query=role+" in " + city +", "+country
    querystring = {"query":query,"num_pages":pg}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("api call sucess ...............................................................")
    new = json.loads(response.text)
    print("json loads sucess...........................................................")
    i=1
    for singleJob in new['data']:
        p= singleJob
        jobId=p['job_id']
        jobTitle=p['job_title']
        companyName =p['employer_name']
        companyUrl =p['employer_website']
        companyLogo =p['employer_logo']
        location =  p['job_city']+','+p['job_state']+','+p['job_country']
        salary = p['job_max_salary']
        applyLink =p['job_apply_link']
        jobdesc=p['job_description']
        jobpublisher=p['job_publisher']
        jobposted=p['job_posted_at_datetime_utc']
        data={'querystring':querystring,'id':jobId,'jobTitle':jobTitle,'companyName':companyName,'companyUrl':companyUrl,"companyLogo":companyLogo,'location':location,'salary':salary,"applyLink":applyLink,'jobdesc':jobdesc,'jobpublisher':jobpublisher,'jobposted':jobposted}

        db2.db.collection(str(id)+str(count)).document(str(i)).set(data)
        i+=1
        print("added success" +" "+str(i))

def fetchDefaultJob(job="PIqeDU2HqZblrez1XIrNJ8f2EHi20"):
    users_ref = db2.db.collection(job)
    docs = users_ref.stream()
    listOfJobs=[]
    for doc in docs:
        num=(doc.id)
        p=doc.to_dict()
        jobId=p['id']
        jobTitle=p['jobTitle']
        companyName =p['companyName']
        companyUrl =p['companyUrl']
        companyLogo =p['companyLogo']
        location =  p['location']
        salary = p['salary']
        applyLink =p['applyLink']
        if job=='defaultJob':
            jobdesc=p['jobDesc']
        else:
            jobdesc=p['jobdesc']
        jobpublisher=p['jobpublisher']
        jobposted=p['jobposted']
        data={'cloudId':num,'id':jobId,'jobTitle':jobTitle,'companyName':companyName,'companyUrl':companyUrl,"companyLogo":companyLogo,'location':location,'salary':salary,"applyLink":applyLink,'jobdesc':jobdesc,'jobpublisher':jobpublisher,'jobposted':jobposted}
        listOfJobs.append(data)
    return(listOfJobs)
