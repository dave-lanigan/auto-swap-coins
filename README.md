# auto-swap-coin [in-dev]

Due to security risks, the centralized nature and high trading fees (percent-based) of many trading plateforms, there have been several decentralized, non-custodial asset exchanges that have come to the fore. [Kyber Network](https://kyber.network/) and [ShapeShift](https://shapeshift.com/?utm_source=shapeshift_classic&utm_medium=homepage_cta) being the most popular. However, although these exchanges have API's, a fully automated transaction between token wallets two wallets, remains impossible.

On top of that, the web3.py usage is fairly complex and the barriar to entry is high and hopefully this package will reduce the complexity of making a transaction somewhat.

The hope of this package is to supply some simple classes/functions to allow for fully automated transactions from one wallet with a private key to another, using a few different possible coin swapping exchanges.

### Installation:
```
```

### Usage:

The package comes with several ETH contract addresses and ABI's in the contrancts folder.

```
```

### Notes:
##### Contract info:
To make a contract json file you must get the the contract address and ABI from Etherscan. The contracts are usually different between token. First, search the token in the etherscann search bar, in the top right you will see the contract address in the "Profile Summary" section. Copy this and add the to the .json file. Then search the address in the search bar of Etherscan. On the page of the search result, find the "Contract" tab. Select it then look for the "Contract ABI" section of the page section. Paste this to the .json file. If this ABI doesn't work, try looking for it on the Github page for the coin.
