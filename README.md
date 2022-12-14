<br />
<div align="center">
    <a href="https://postimg.cc/N2ff3Q88"><img src="https://i.postimg.cc/Xq9GyJpP/M.gif" alt="Add-a-heading" border="0" width="200" height="200"></a>
  <h3 align="center">MoralisSDK</h3>
 
</div>

## Problem
1. Data analytics and Data related projects for web3 protocols increasing day by day but lack of sdk//wrapper//easy to use functions available for protocols in python language.

2. No easy to use tools on python for NFTStorage // web3storage // pinata // MoralisIPFS.

## Solution
  
  ***MoralisSDK** is a DATA DEVELOPER TOOLING

1. It provide a easy to integrate methods to get the datas very quickly with the help of Moralis.

2. Simple function's for NFTSTORAGE,WEB3STORAGE,PINATA upload and download options in python.

3. It provide chainlink analytics data via simple function call with the help of Moralis.


## Moralis
Use requires a Molaris API key which is currently available with the free Molaris service tier. 
- https://moralis.io/
- https://deep-index.moralis.io/api-docs/#/
- https://docs.moralis.io/moralis-server/web3-sdk/moralis-web3-api-rest


# Install

    ** pip install MoralisSDK==1.0.1

## IPFS Setup
    from MoralisSDK import ipfs
    moralis = ipfs.IPFS()
    

## NFTSTORAGE

1.upload_nft_storage(api_key,file)

2.status_nft_storage(apikey,cid)

3.nft_storage_download_link(cid)

## WEB3STORAGE

1.upload_web3_storage(apikey,file)

2.status_web3_storage(apikey,cid)

3.web3_storage_download_link(cid)

## PINATA

1.upload_pinata(pinata_api_key,pinata_secret_api_key, file)

2.pinata_download_link(cid)



## MORALIS Setup

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
    
    

## CHAINLINK Setup

    from MoralisSDK import chainlink
    moralis = chainlink.Chainlink()

## Available functions to get Chainlink analytics data

offset -> page , limit -> data points limit, sortby -> [asc, desc]

1.active_feeds(offset,limit)

2.Active_Feeds_Requesters(limit, sortby)

3.Keepers_BSC_Daily(limit, sortby)

4.Keepers_ETH_Daily(limit, sortby)

5.Keepers_POLYGON_Daily(limit, sortby)

6.Oracle_Requests_over_Time(limit, sortby)

7.Total_LINK_on_centralized_exchanges(limit, sortby)

8.chainlink_VRF_v1_daily_BSC(limit, sortby)

9.chainlink_VRF_v1_daily_ETH(limit, sortby)

10.chainlink_VRF_v1_daily_POLYGON(limit, sortby)

11.chainlink_VRF_v2_daily_BSC(limit, sortby)

12.chainlink_VRF_v2_daily_ETH(limit, sortby)

13.chainlink_VRF_v2_daily_POLYGON(limit, sortby)



## End Notes

MoralisSdk that capable to help the data analyst or data scientiest who works on web3 analytics.Just make the flow very easy for them to develop the projects.

MoralisSDK still ongoing with the development to add more web3 protocols data's with the help of Moralis.

