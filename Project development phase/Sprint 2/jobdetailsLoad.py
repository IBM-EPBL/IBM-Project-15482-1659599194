from auth import db2 

def findJobDetails(cloudId,user="defaultJob"):
    users_ref = db2.db.collection(user)
    docs = users_ref.stream()
    listOfJobs=[]
    for doc in docs:
        if doc.id==cloudId:
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
            if user=='defaultJob':
                jobdesc=p['jobDesc']
            else:
                jobdesc=p['jobdesc']
            jobpublisher=p['jobpublisher']
            jobposted=p['jobposted']
            data={'cloudId':num,'id':jobId,'jobTitle':jobTitle,'companyName':companyName,'companyUrl':companyUrl,"companyLogo":companyLogo,'location':location,'salary':salary,"applyLink":applyLink,'jobdesc':jobdesc,'jobpublisher':jobpublisher,'jobposted':jobposted}
            listOfJobs.append(data)
            break 
        
    return(listOfJobs)