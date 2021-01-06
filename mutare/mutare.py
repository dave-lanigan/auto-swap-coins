from kybernet.client import Klient
#from shapeshift import ShapeShift
from web3 import Web3
import json


class KyberSwap(Klient):

    def __init__(self,node_endpoint="",pair):
        """Need to with a pair"""
        super().__init__()
        if node_endpoint="":
            f=open(CONFIG_PATH+"config.json","r")
            config=json.load(f)
            f.close()
            web3 = Web3(Web3.HTTPProvider( config["infura"]["endpoint_https"] ))
        elif node_endpoint != "":
            web3=Web3(Web3.HTTPProvider( node_endpoint))

        pair=pair.split("_")
        src_symbol,dst_symbol=pair[0].lower(),pair[1].lower()

        f=open(CONFIG_PATH+"contracts.json","r")
        contracts=json.load(f)
        f.close()
        
        self.web3=web3
        self.src_symbol=src_symbol
        self.dst_symbol=dst_symbol
        self.src_contract=web3.eth.contract(address=contracts[src_symbol]["address"],
                          abi=contracts[symbol]["abi"])
        self.dst_contract=web3.eth.contract(address=contracts[src_symbol]["address"],
                          abi=contracts[symbol]["abi"])


    def init_convert(self,source_address,qty,min_dst_qty):
        """Initializes the information needed for a transaction based on the pair given.
        Arguments:
            source_address {string}: 
            qty
        Returns:
            Transaction dictionory.
        """

        ####----
        #split pair
        ## deal with slippage here
        pair=self.src_symbol+"_"+self.dst_symbol
        tx=self.trade_data(source_addr,pair,qty,min_dst_qty)["data"][0]
        if tx["from"]==source_address:
            tx={"nonce":tx["nonce"],
                "to":tx["to"], 
                "value":tx["value"],
                "data":tx["data"],
                "gas":tx["gasLimit"],
                "gasPrice":tx["gasPrice"] }
        
        self.tx=tx
        self.source_address=source_address
        return tx

    
    def init_transfer(self,source_wallet,to_wallet,pair):
        self.pair=pair
        self.from_wallet=from_wallet
        self.to_wallet=to_wallet



    def check_gas(self,tx={}):
        if tx is None:
            tx=self.tx
        
        gas=web3.toInt( hexstr=tx["gasLimit"] )
        gas_price= web3.fromWei( web3.toInt( hexstr=tx["gasPrice"] ), "ether" )
        gas_price_gwei= web3.fromWei( web3.toInt( hexstr=tx["gasPrice"] ), "gwei" )

        print("Current price in Ether: {}".format(gas*gas_price) )
        
        return gas, gas_price_gwei

    def transact(self,pkey):
        signed_txn = web3.eth.account.signTransaction(self.tx, pkey)
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return web3.toHex(txn_hash)

    def check_balance(self,address="source"):
        if address=="source":
            address=self.source_address
            c=self.src_contract
        elif address="destination":
            address=self.destination_address
            c=self.dst_contract

        DECIMALS = 10**c.functions.decimals().call()
        bal=c.functions.balanceOf(address).call()/DECIMALS
        token_name=c.functions.name().call()

        return [token_name, bal]

    def gas_and_slip_rules(self):
        pass



# class Shift(ShapeShift):

#     def __init__(self, endpoint):
#         """Need to with a pair"""
#         super().__init__()
#         self.web3=Web3(Web3.HTTPProvider( endpoint))
    
#     def init_transaction(self,pair,from_wallet,to_wallet):
#         self.pair=pair
#         self.from_wallet=from_wallet
#         self.to_wallet=to_wallet
        


     
