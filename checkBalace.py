from armoryengine.ALL import *

wlt = PyBtcWallet().readWalletFile( CLI_ARGS[0] )

# Register wallet and start blockchain scan
TheBDM.registerWallet(wlt)
TheBDM.setBlocking(True)
TheBDM.setOnlineMode(True)  # will take 20 min for rescan

# Need "syncWithBlockchain" every time TheBDM is updated
wlt.syncWithBlockchain()

# THe wallet now holds all relevent blockchain data
print 'Wallet balance information:'
print '   Bal 0+ conf:', coin2str(wlt.getBalance('Full'))
print '   Bal >0 conf:', coin2str(wlt.getBalance('Spendable'))
print '   Bal >5 conf:', coin2str(wlt.getBalance('Unconfirmed'))
utxoList = list(wlt.getTxOutList('Spendable'))
pprintUnspentTxOutList(utxoList, 'Example Unspent TxOutList')

TheBDM.execCleanShutdown()
