from armoryengine.ALL import *
filename  = r"C:\Users\Administrator\AppData\Roaming\Armory\armory_2VQoCWtYP_backup.wallet"
globals()["PyBtcWallet"]
wlt = PyBtcWallet().readWalletFile(filename)
address= wlt.getNextUnusedAddress().getAddrStr()
print address