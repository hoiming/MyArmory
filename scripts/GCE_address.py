#! /usr/bin/python
from armoryengine.ALL import *
filename=r"C:\Users\Administrator\AppData\Roaming\Armory\armory_2VQoCWtYP_backup.wallet"

addr='184V1PQCVzqqC19VaiBbuoZVDFdKCo5JLX'
addrObj1=addrStr_to_hash160(addr,True)
if addrObj1 is None:
    print 'fail'
else:
    print 'good'

print addrObj1
#addr1=hash160_to_addrStr(addrObj1)
#print addr1
#addrObj=addrObj(addr)
#addrObj=PyBtcAddress().createFromAddrStr(addr)
#print addrObj1.calculateAddrStr()
#addr160=addrObj.getAddr160()
#print addr160
print 'ffffffff'
