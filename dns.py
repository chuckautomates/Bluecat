import requests
import json
from base import Base as Base

class DNS(Base):

    def __init__(self, **kwargs):
        self._base = '{0}{1}{2}'.format('https://', kwargs['hfBamIp'], '/Services/REST/v1')
        self._username = kwargs['username']
        self._password = kwargs['password'] 
        # self._ = ''
        # self._base_ = Base()


    def createDnsRecord(self, hostname, ipAddress):
        xpath = '{0}{1}'.format(self._base, '/addEntity?parentId=100895')
        properties = '{0}{1}{2}{3}{4}'.format('absoluteName=', hostname, 
                    '.healthfirst.org|addresses=', 
                    ipAddress, '|reverseRecord=true|')
        body =  {'name': hostname,
                'type': 'HostRecord',
                'properties': properties}
        jsonBody = json.dumps(body)
        #print(jsonBody)
        token = self.generateToken()
        headers = self.headers(token)
        #print(headers)
        response = self.postRequest(xpath, headers, jsonBody, False)
        #print(response.text)
        check = self.request200check(response.status_code)
        if check == True:
            returnDict = {'ObjectId': response.text}
            returnJson = json.dumps(returnDict)
            return(returnJson)
        else:
            return(response.status_code, response.reason)
