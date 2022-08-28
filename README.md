# MoralisSDK
## Introduction
A simple Python sdk for the Moralis Native, Account and Token apis ['yet to add more']. It helps by calling simple function to get the data that really helpful for data analytics. 

## Moralis
Use requires a Molaris API key which is currently available with the free Molaris service tier. 
- https://moralis.io/
- https://deep-index.moralis.io/api-docs/#/
- https://docs.moralis.io/moralis-server/web3-sdk/moralis-web3-api-rest

# Install

    ** pip install MoralisSDK==1.0.1
## Setup

Replace YOUR_API_KEY with the Moralis API Key.

    from MoralisSDK import api
    moralis = api.MoralisApi()
    moralis.set_api_key("YOUR_API_KEY")


## Get_nfts [Account] (Function shows manditory params, play around with optional also).

    moralis.get_nfts(address='0x1d62df39f4D20119EcEEf66bFEE23c0afe49CeB8', chain='eth')

## Get_transfers [Account].

    moralis.get_nfts_transfer(address='0x1d62df39f4D20119EcEEf66bFEE23c0afe49CeB8', chain='eth')

## Get_nft_for_contract [Account].

    moralis.get_nfts_token(address='0x73E9f114536C6807B6d9388bBf76f5404c621a77', chain='eth', token_address='0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258')

## Get_nft_trade [Token].

    moralis.get_nfts_trades(address='0x73E9f114536C6807B6d9388bBf76f5404c621a77', chain='eth')

## Get_nft_lowest_price [Token].

    moralis.get_nft_lowest_price(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', chain='eth')

## Get_nft_transfer_from_blocks [Token].

    moralis.get_nfts_transfer_blocks(from_block='***')

## Get_tokenids [Token].

    moralis.get_token_id(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d')

## Get_nft_owners [Token].

    moralis.get_nft_owners(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d')

## Get_nft_contract_transfer [Token].

    moralis.get_contract_nft_transfers(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d')

## Get_nft_collection_metadata [Token].

    moralis.get_nft_metadata(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d')

## Check_nft_metadata_sync [Token].

    moralis.get_nft_metadata_resync(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', token_id='1000')

## Get_nft_token_metadata [Token].

    moralis.get_token_id_metadata(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', token_id='1000')

## Get_nft_token_owner [Token].

    moralis.get_token_id_owners(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', token_id='1000')

## Get_nft_transfer [Token].

    moralis.get_token_id_transfers(address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', token_id='1000')
    
## Get_native_balance

    moralis.get_native_balance(address, chain)

## Get_tokens_for_wallet

    moralis.get_tokens_for_wallet(address, chain)

## Get_token_price

    moralis.get_token_price(address, chain)

## Native_to_token

    moralis.convert_native_amount_to_token_amount(address, chain, native_amount)

## Token_to_native

    moralis.convert_token_amount_to_native_amount(address, chain, native_amount)
    
    
