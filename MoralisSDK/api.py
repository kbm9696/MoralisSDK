import requests
import datetime

QueryParameter = ['?', '&']


class MoralisApi:
    def __init__(self):
        self.url_base = 'https://deep-index.moralis.io/api/v2/'
        self.api_key = None

    def set_api_key(self, api_key):
        self.api_key = api_key

    def api_request(self, endpoint, method="GET", request_data=None):
        try:
            headers = {
                "x-api-key": self.api_key
            }
            response = requests.request(url=self.url_base + endpoint, method=method, headers=headers, data=request_data)
            if response.status_code == 200:
                response_object = response.json()
                # response_object['status_code'] = 200
                return response_object
            elif response.status_code == 404:
                return f'{self.url_base}{endpoint} is not found'
            else:
                return response.json()
        except Exception as err:
            print(f'Got Exception :{err}')

    def get_nfts(self, address, chain=None, token_format='decimal', limit=None, token_addresses=None, cursor=None):
        endpoint = ''
        if address:
            if type(address) == str and len(address):
                endpoint = f'{address}/nft?token_format={token_format}'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'

            if token_addresses is not None:
                if type(token_addresses) != list:
                    print('token_format Argument Type Error')
                    return TypeError('Argument Type Error: token_addresses must be list')
                for k in token_addresses:
                    endpoint += f'&token_addresses={k}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
        else:
            print('Required argument missing either address')
            return TypeError('Argument Type Error: address must be str')

        response = self.api_request(endpoint)
        return response

    def get_nfts_transfer(self, address, chain=None, token_format='decimal', limit=None, direction=None,
                          from_block=None,
                          to_block=None, cursor=None):
        endpoint = ''
        if address:
            if type(address) == str and len(address):
                endpoint = f'{address}/nft/transfers?format={token_format}'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'
            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'

            if direction is not None:
                if type(direction) != str and direction not in ['both', 'to', 'from']:
                    print('direction Argument Type Error or Invalid value')
                    return TypeError('Argument Type Error: direction must be str')
                endpoint += f'&direction={direction}'
            if from_block is not None:
                if type(from_block) != str:
                    print('from_block Argument Type Error')
                    return TypeError('Argument Type Error: from_block must be str')
                endpoint += f'&from_block={from_block}'
            if to_block is not None:
                if type(to_block) != str:
                    print('to_block Argument Type Error')
                    return TypeError('Argument Type Error: to_block must be str')
                endpoint += f'&to_block={to_block}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'

        else:
            print('Required argument missing either address')
            return TypeError('Argument Type Error: address must be str')

        response = self.api_request(endpoint)
        return response

    def get_nfts_token(self, address, chain=None, token_format='decimal', limit=None, token_address=None, cursor=None):
        endpoint = ''
        if address and token_address:
            if type(address) == str and len(address):
                if type(token_address) == str and len(token_address):
                    endpoint = f'{address}/nft/{token_address}?format={token_format}'
                else:
                    print('token_address Argument Type Error')
                    return TypeError('Argument Type Error: token_address must be str')
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')

            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'

            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
        else:
            print('Required argument missing either token_address or address')
            return TypeError('Argument Type Error: address and token_address must be str')
        response = self.api_request(endpoint)
        return response

    def get_nfts_trades(self, address, chain=None, limit=None, from_block=None,
                        to_block=None, from_date=None, to_date=None, provider_url=None, marketplace='opensea',
                        cursor=None):
        endpoint = ''
        if address:
            if type(address) == str and len(address):
                endpoint = f'nft/{address}/trades?marketplace={marketplace}'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'

            if from_block is not None:
                if type(from_block) != str:
                    print('from_block Argument Type Error')
                    return TypeError('Argument Type Error: from_block must be str')
                endpoint += f'&from_block={from_block}'
            if to_block is not None:
                if type(to_block) != str:
                    print('to_block Argument Type Error')
                    return TypeError('Argument Type Error: to_block must be str')
                endpoint += f'&to_block={to_block}'
            if from_date is not None:
                if type(from_date) != str:
                    print('from_date Argument Type Error')
                    return TypeError('Argument Type Error: from_date must be str')
                endpoint += f'&from_date={from_date}'
            if to_date is not None:
                if type(to_date) != str:
                    print('to_date Argument Type Error')
                    return TypeError('Argument Type Error: to_date must be str')
                endpoint += f'&to_date={to_date}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
            if provider_url is not None:
                if type(provider_url) != str:
                    print('provider_url Argument Type Error')
                    return TypeError('Argument Type Error: provider_url must be str')
                provider_url += f'&provider_url={provider_url}'
        else:
            print('Required argument missing address')
            return TypeError('Argument Type Error: address must be str')

        response = self.api_request(endpoint)
        return response

    def get_nft_lowest_price(self, address, chain=None, days=None, provider_url=None, marketplace='opensea'):
        endpoint = ''
        if address:
            if type(address) == str and len(address):
                endpoint = f'nft/{address}/lowestprice?marketplace={marketplace}'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'
            if days is not None:
                if type(days) != int:
                    print('days Argument Type Error')
                    return TypeError('Argument Type Error: days must be str')
                endpoint += f'&days={days}'
            if provider_url is not None:
                if type(provider_url) != str:
                    print('provider_url Argument Type Error')
                    return TypeError('Argument Type Error: provider_url must be str')
                provider_url += f'&provider_url={provider_url}'
        else:
            print('Required argument missing address')
            return TypeError('Argument Type Error: address must be str')
        print(endpoint)
        response = self.api_request(endpoint)
        return response

    def get_nfts_transfer_blocks(self, chain=None, token_format='decimal', limit=None, from_block=None, to_block=None,
                                 from_date=None, to_date=None, cursor=None):
        endpoint = f'nft/transfers?format={token_format}'
        if chain is not None:
            if type(chain) != str:
                print('chain Argument Type Error')
                return TypeError('Argument Type Error: chain must be str')
            endpoint += f'&chain={chain}'
        if limit is not None:
            if type(limit) != int:
                print('limit Argument Type Error')
                return TypeError('Argument Type Error: limit must be int')
            endpoint += f'&limit={limit}'

        if from_block is not None:
            if type(from_block) != str:
                print('from_block Argument Type Error')
                return TypeError('Argument Type Error: from_block must be str')
            endpoint += f'&from_block={from_block}'
        if to_block is not None:
            if type(to_block) != str:
                print('to_block Argument Type Error')
                return TypeError('Argument Type Error: to_block must be str')
            endpoint += f'&to_block={to_block}'
        if from_date is not None:
            if type(from_date) != str :
                print('from_date Argument Type Error')
                return TypeError('Argument Type Error: from_date must be str')
            endpoint += f'&from_date={from_date}'
        if to_date is not None:
            if type(to_date) != str:
                print('to_date Argument Type Error')
                return TypeError('Argument Type Error: to_date must be str')
            endpoint += f'&to_date={to_date}'
        if cursor is not None:
            if type(cursor) != str:
                print('cursor Argument Type Error')
                return TypeError('Argument Type Error: cursor must be str')
            endpoint += f'&cursor={cursor}'

        response = self.api_request(endpoint)
        return response

    def get_token_id(self, address, chain=None, token_format='decimal', limit=None, total_range=None, subrange=None,
                     cursor=None):
        endpoint = ''
        if address:
            if type(address) == str and len(address):
                endpoint = f'nft/{address}?token_format={token_format}'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'

            if total_range is not None:
                if type(total_range) != int:
                    print('total_range Argument Type Error')
                    return TypeError('Argument Type Error: total_range must be int')
                endpoint += f'&total_range={total_range}'
            if subrange is not None:
                if type(subrange) != int:
                    print('range Argument Type Error')
                    return TypeError('Argument Type Error: subrange must be int')
                endpoint += f'&range={subrange}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
        else:
            print('Required argument missing address')
            return TypeError('Argument Type Error: address must be str')

        response = self.api_request(endpoint)
        return response

    def get_nft_owners(self, address, chain=None, token_format='decimal', limit=None, cursor=None):
        endpoint = ''
        if address:
            if type(address) == str and len(address):
                endpoint = f'nft/{address}/owners?token_format={token_format}'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
        else:
            print('Required argument missing address')
            return TypeError('Argument Type Error: address must be str')

        response = self.api_request(endpoint)
        return response

    def get_contract_nft_transfers(self, address, chain=None, token_format='decimal', limit=None, cursor=None):
        endpoint = ''
        if address:
            if type(address) == str:
                endpoint = f'nft/{address}/transfers?token_format={token_format}'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
        else:
            print('Required argument missing address')
            return TypeError('Argument Type Error: address must be str')

        response = self.api_request(endpoint)
        return response

    def get_nft_metadata(self, address, chain=None):
        endpoint = ''
        if address:
            if type(address) == str and len(address):
                endpoint = f'nft/{address}/metadata'
            else:
                print('address Argument Type Error')
                return TypeError('Argument Type Error: address must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'
        else:
            print('Required argument missing address')
            return TypeError('Argument Type Error: address must be str')

        response = self.api_request(endpoint)
        return response

    def get_nft_metadata_resync(self, address, token_id, chain=None, flag='uri', mode='sync'):
        endpoint = ''
        if address and token_id:
            if type(token_id) == str and len(token_id):
                if type(address) == str and len(address):
                    if type(mode) == str and type(flag) == str:
                        endpoint = f'nft/{address}/{token_id}/metadata/resync?mode={mode}&flag={flag}'
                    else:
                        print('mode or flag type error')
                else:
                    print('address Argument Type Error')
                    return TypeError('Argument Type Error: address must be str')
            else:
                print('token_id Argument Type Error')
                return TypeError('Argument Type Error: token_id must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

        else:
            print('Required argument missing either token_id or address')
            return TypeError('Argument Type Error: address and token_id must be str')

        response = self.api_request(endpoint)
        return response

    def get_token_id_metadata(self, address, token_id, chain=None, token_format='decimal'):
        endpoint = ''
        if address and token_id:
            if type(token_id) == str and len(token_id):
                if type(address) == str and len(address):
                    if type(token_format) == str:
                        endpoint = f'nft/{address}/{token_id}?format={token_format}'
                    else:
                        print('token format type error')
                else:
                    print('address Argument Type Error')
                    return TypeError('Argument Type Error: address must be str')
            else:
                print('token_id Argument Type Error')
                return TypeError('Argument Type Error: token_id must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'

        else:
            print('Required argument missing either token_id or address')
            return TypeError('Argument Type Error: address/token_id must be str')

        response = self.api_request(endpoint)
        return response

    def get_token_id_owners(self, address, token_id, chain=None, token_format='decimal', limit=None, cursor=None):
        endpoint = ''
        if address and token_id:
            if type(token_id) == str and len(token_id):
                if type(address) == str and len(address):
                    if type(token_format) == str:
                        endpoint = f'nft/{address}/{token_id}/owners?format={token_format}'
                    else:
                        print('token format type error')
                else:
                    print('address Argument Type Error')
                    return TypeError('Argument Type Error: address must be str')
            else:
                print('token_id Argument Type Error')
                return TypeError('Argument Type Error: token_id must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'

        else:
            print('Required argument missing either token_id or address')
            return TypeError('Argument Type Error: token_id/address must be str')

        response = self.api_request(endpoint)
        return response

    def get_token_id_transfers(self, address, token_id, chain=None, order=None, token_format='decimal', limit=None,
                               cursor=None):
        endpoint = ''
        if address and token_id:
            if type(token_id) == str and len(token_id):
                if type(address) == str and len(address):
                    if type(token_format) == str:
                        endpoint = f'nft/{address}/{token_id}/owners?format={token_format}'
                    else:
                        print('token format type error')
                else:
                    print('address Argument Type Error')
                    return TypeError('Argument Type Error: address must be str')
            else:
                print('token_id Argument Type Error')
                return TypeError('Argument Type Error: token_id must be str')
            if chain is not None:
                if type(chain) != str:
                    print('chain Argument Type Error')
                    return TypeError('Argument Type Error: chain must be str')
                endpoint += f'&chain={chain}'
            if cursor is not None:
                if type(cursor) != str:
                    print('cursor Argument Type Error')
                    return TypeError('Argument Type Error: cursor must be str')
                endpoint += f'&cursor={cursor}'
            if limit is not None:
                if type(limit) != int:
                    print('limit Argument Type Error')
                    return TypeError('Argument Type Error: limit must be int')
                endpoint += f'&limit={limit}'
            if order is not None:
                if type(order) != str:
                    print('order Argument Type Error')
                    return TypeError('Argument Type Error: order must be str')
                endpoint += f'&order={order}'

        else:
            print('Required argument missing either token_id address')
            return TypeError('Argument Type Error: address/token_id must be str')

        response = self.api_request(endpoint)
        return response