# MoralisSDK
## Introduction
A simple Python wrapper for the Molaris REST API. Useful for getting ERC-20 token prices, getting general token information and getting information about all tokens in a wallet. 

## Molaris
Use requires a Molaris API key which is currently available with the free Molaris service tier. 
- https://moralis.io/
- https://deep-index.moralis.io/api-docs/#/
- https://docs.moralis.io/moralis-server/web3-sdk/moralis-web3-api-rest

# Usage
## Setup

Replace YOUR_API_KEY with the Moralis API Key.

    from MoralisSDK.api import MoralisAPI
    moralis = MoralisAPI()
    moralis.set_api_key("YOUR_API_KEY")
