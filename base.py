import requests
import json



class Base():
    def __init__(self, **kwargs):
        self._base = '{0}{1}{2}'.format('https://', kwargs['hfBamIp'], '/Services/REST/v1')
        self._username = kwargs['username']
        self._password = kwargs['password']


    def request200check(self, statusCode):
        if statusCode == 200:
            return(True)
        else:
            return(False)

    def headers(self, token):
        headers = {'Authorization': token,
                    'Content-Type': 'application/json'}
        return(headers)

    def postRequest(self, xpath, headers, body, sslVerify):
        try:
            response = requests.request("POST", xpath, headers = headers, verify = sslVerify, data=body)
            #print(response)
        except:
            response = requests.request("POST", xpath, headers = headers)
        return(response)

    def generateToken(self):
        xpath = '{0}{1}{2}{3}{4}'.format(self._base, '/login?username=', self._username, '&password=', self._password)
        response = requests.request("GET", xpath, verify = False)
        check = self.request200check(response.status_code)
        if check == True:
            returnString = response.json()
            split = returnString.split('BAMAuthToken: ')
            token = split[1].split(' <-')
            return(token[0])
        else:
            returnDict = {'Status': 'Failed', 
                        'StatusCode': response.status_code, 
                        'Reason': 'Reieved non 200 on generateToken'}
            returnJson = json.dumps(returnDict)
            return(returnJson)
