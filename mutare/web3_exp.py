from web3 import Web3
import json


##-------opening example

eth_addr="0xFE9b25750A078fe4B5BbbDFD7ce362Ed80Dc1272"

f=open("c.json","r")
c=json.load(f)
f.close

endpoint=c["data"]["endpoint_https"]

#connect to the blockchain
web3 = Web3(Web3.HTTPProvider(endpoint))

print(web3.isConnected())
wei=web3.eth.getBalance(eth_addr)
print( web3.fromWei(wei,"ether") )



##-------sending transactions

#build a transactions
#sign transactions
#send transactions
#get transaction has

#nonce prevents sending transaction again

#nonce=

#tx={"nonce":"","to":"","value":,"gas":}

#web3.eth.account.signTransaction(tx,private_key)
#web3.eth.account.sendRawTransaction(tx,private_key)








