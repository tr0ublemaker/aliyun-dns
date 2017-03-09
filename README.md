# aliyun-dns
a python script to change website's IP address with aliyun-SDK 

可以修改家中动态ip指向固定域名的解决方案

1.使用crontab循环调用main.py
2.注意key.json的保密（管理员权限）
3.修改api/rest/Dns20150109DescribeDomainRecordInfoRequest.py和Dns20150109UpdateDomainRecordRequest.py
下的  `recordId=*-*`
4.recordid的获取方式可以在阿里云登录状态下 使用chrome开发工具抓包其中可以找到 recordid
