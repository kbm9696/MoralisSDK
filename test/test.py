from MoralisSDK import api
from time import sleep
if __name__ == '__main__':
    t = api.MoralisApi()
    t.set_api_key('L1aTPccpZTZpCTcRCMyCinajCny6uIMKKYT7we5L9ReQ7cSd53jm4npzQoE0NgkW')
    nft = t.get_nfts(address='0x260fCF88102fB038B2506dC60fc49270199e12fE')
    print(nft)
    ntf_trans = t.get_nfts_transfer(address='0x260fCF88102fB038B2506dC60fc49270199e12fE')
    print(ntf_trans)
    res = t.get_nfts_token(chain='eth',address='0x260fCF88102fB038B2506dC60fc49270199e12fE',
                           token_address='0xd07dc4262bcdbf85190c01c996b4c06a461d2430',limit=3)
    print(res)
    lowest = t.get_nft_lowest_price(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d',days=5)
    print(lowest)
    transfer = t.get_nfts_transfer_blocks(from_block='12895140')
    print(transfer)
    token = t.get_token_id(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d',total_range=2)
    print(token)
    owners = t.get_nft_owners(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d',limit=1)
    print(owners)
    contract_trasfers = t.get_contract_nft_transfers(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d')
    print(contract_trasfers)
    sleep(10)
    resync = t.get_nft_metadata_resync(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d',token_id='430')
    print(resync)
    token_meta = t.get_token_id_metadata(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d',token_id='430')
    print(token_meta)
    token_owners = t.get_token_id_owners(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d',token_id='432')
    print(token_owners)
    token_trans = t.get_token_id_transfers(address='0x73f1780cb2b5ce961601fdf6a9b002082bb82b4d',token_id='430')
    print(token_trans)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
