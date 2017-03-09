import aliyun.api
import urllib2
import json
import codecs
import time

class DNS:
    jsonfile = file('key.json')
    s = json.load(jsonfile)
    aliyun.setDefaultAppInfo(str(s['id']),str(s['secret']))
    def getDNSIp(self):
        b = aliyun.api.Dns20150109DescribeDomainRecordInfoRequest()
        try:
            f = b.getResponse()
            return (str(f.get('Value')))
        except Exception,e:
            print('getDNSIp:',e)
            return None

    def getMyIp(self):
        try:
            u = urllib2.urlopen('http://members.3322.org/dyndns/getip')
            return u.read().strip('\n')
        except urllib2.HTTPError as e:
            print('getMyIp:',e)
            return None;

    def main(self,newIp):
        a = aliyun.api.Dns20150109UpdateDomainRecordRequest(newIp);
        a.DBInstanceId = ""
        try:
            print("start")
            f = a.getResponse();
            print(f)
        except Exception , e:
            print('main:',e)


if __name__ =='__main__':
    d = DNS()
    oldip = d.getDNSIp()
    newip = d.getMyIp()
    print('oldIp:', oldip)
    with codecs.open('log.csv', 'a','utf-8') as f_in:
        if(oldip != newip and oldip is not None):
            print('oldIp:',oldip)
            print('newIp:',newip)
            d.main(newip)
            f_in.write('{}{}'.format(newip, time.ctime()))