#! /usr/bin/python
from armoryengine.ALL import *
'''filename=r"C:\Users\Administrator\AppData\Roaming\Armory\armory_2VQoCWtYP_backup.wallet"
wlt = PyBtcWallet().readWalletFile( filename )

# Register wallet and start blockchain scan
TheBDM.registerWallet(wlt)
print 'aaaaaaaaaaaaaaaaaaaaaaaaaa'
TheBDM.setBlocking(True)
print 'bbbbbbbbbbbbbbbbbbb'
TheBDM.setOnlineMode(True)  # will take 20 min for rescan
print 'cccccccccccccccccc'

# Need "syncWithBlockchain" every time TheBDM is updated
wlt.syncWithBlockchain()
print 'ddddddddddddddddddddddddddddd'


addr='1EQG9WUJTCQw3tmoNXuLybvjkAZDSFFjrQ'

scrAddr = addrStr_to_scrAddr(addr)
addr160 = scrAddr_to_hash160(scrAddr)[1]


spendBal = wlt.getAddrBalance(addr160, 'Spendable', 320000)

print 'eeeeeeeeeeeeeeeeeee'
#print coin2str(spendBal)
print spendBal'''


def initilzeWallet(filename=r"C:\Users\Administrator\AppData\Roaming\Armory\armory_2VQoCWtYP_backup.wallet"):
    wlt = PyBtcWallet().readWalletFile(filename)
    TheBDM.registerWallet(wlt)
    TheBDM.setBlocking(True)
    TheBDM.setOnlineMode(True)
    wlt.syncWithBlockchain()
    return wlt


def getAddressBalanceDict(wlt, addressList=[]):

    addrBaDict = {}

    for addr in addressList:
        scrAddr = addrStr_to_scrAddr(addr)
        addr160 = scrAddr_to_hash160(scrAddr)[1]
        spendBal = wlt.getAddrBalance(addr160, 'Spendable', 320000)
        addrBaDict[addr] = spendBal

    return addrBaDict

try:

    wallet = initilzeWallet()
    addrList = ['1EQG9WUJTCQw3tmoNXuLybvjkAZDSFFjrQ']
    abDict = getAddressBalanceDict(wallet, addrList)
except Exception, e:
    print 'Error - ', e
finally:
    TheBDM.execCleanShutdown()

print abDict['1EQG9WUJTCQw3tmoNXuLybvjkAZDSFFjrQ']