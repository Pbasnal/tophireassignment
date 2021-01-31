import codecs
from pycookiecheat import chrome_cookies
import requests
from applicant import applicant
from headers import headers
from attachment import attachment
import os
import datetime
import json
from datetime import datetime, tzinfo, timedelta
from hyper.contrib import HTTP20Adapter
from requests_toolbelt.utils import dump
import zlib


print("----------Building Resume Payload--------------")
class simple_utc(tzinfo):
    def tzname(self,**kwargs):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)

uploadDate = datetime.utcnow().replace(tzinfo=simple_utc()).isoformat().replace('+00:00', 'Z')

with open('attachment_formdata', 'r') as file:
    data = file.read()#.replace('\n', '')

data = data.replace("<resumename>", "testresume.odt")
data = data.replace("<resumetype>", "application/vnd.oasis.opendocument.text")
data = data.replace("<resumesize>", str(os.stat('testresume.odt').st_size))
data = data.replace("<updatetime>", uploadDate)

#print(data)

print("----------Captuing Cookies--------------")
url = 'https://tophire.freshteam.com/dashboard/me'
cookies = chrome_cookies(url)
print(cookies)

print("----------Creating Entry for the Resume--------------") 
resumeUrl = "https://tophire.freshteam.com/attachments"



files ={"attachment": open("testresume.odt", 'rb')}

attachment = {
    "content_file_name": "testresume.odt",
    "content_content_type": "application/vnd.oasis.opendocument.text",
    "content_file_size": str(os.stat('testresume.odt').st_size),
    "content_updated_at": uploadDate,
    #"content": hex_data,
    "description": "resume",
    "skip_parsing": False
}



def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print("----------Response Code--------------")
    #body = zlib.decompress(data, 16+zlib.MAX_WBITS)
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body.decode("latin-1"),
    ))


# req = requests.Request('POST', resumeUrl, files=files, cookies=cookies, headers=headers)
# prepared = req.prepare()
# pretty_print_POST(prepared)



# r = requests.post(resumeUrl, files=files, cookies=cookies, headers=headers)
# #print(r.text)
# print("----------Response Code--------------")

# data = dump.dump_all(r)
# print(zlib.decompress(data, 16+zlib.MAX_WBITS))
# print(r)

with requests.session() as sess:
    sess.mount(resumeUrl, HTTP20Adapter())
    r = sess.post(resumeUrl, files=files, cookies=cookies, headers=headers)
    print(r.text)
    print("----------Response Code--------------")
    print(r)

exit()




#attachment["content"] = hex_data
# url = 'https://tophire.freshteam.com/hire/jobs/3000023633/applicants'



os.stat('testresume.odt').st_size

#print(hex_data)

print(applicant["lead_attributes"]["email"])
applicant["lead_attributes"]["email"] = "democandidate1234@gmail.com" 
applicant["lead_attributes"]["first_name"] = "demo1" 
applicant["lead_attributes"]["last_name"] = "candi1" 
applicant["lead_attributes"]["resumes_attributes"]["content_file_size"] = os.stat('testresume.odt').st_size
applicant["lead_attributes"]["resumes_attributes"]["content_content_type"] = "application/vnd.oasis.opendocument.text"
applicant["lead_attributes"]["resumes_attributes"]["content_file_name"] = "testresume.odt"

applicant["lead_attributes"]["resumes_attributes"]["content_updated_at"] = uploadDate

print(applicant["lead_attributes"]["resumes_attributes"])
applicant["lead_attributes"]["resumes_attributes"]["content"] = hex_data




req = requests.Request('POST',resumeUrl, json=attachment, cookies=cookies)
prepared = req.prepare()



#jobsUrl = "https://tophire.freshteam.com/hire/jobs"
#r = requests.get(jobsUrl, cookies=cookies)
#print("\n\n Jobs Urls ")
#print(r)
#print(r.text)
