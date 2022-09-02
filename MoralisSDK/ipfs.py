import time
from urllib import response
from pinatapy import PinataPy
import nft_storage
from nft_storage.api import nft_storage_api
from nft_storage.model.error_response import ErrorResponse
from nft_storage.model.upload_response import UploadResponse
from nft_storage.model.unauthorized_error_response import UnauthorizedErrorResponse
from nft_storage.model.forbidden_error_response import ForbiddenErrorResponse
from pprint import pprint
import requests



class IPFS:
    def __init__(self):
        pass

    def upload_nft_storage(apikey,file):
         # See configuration.py for a list of all supported configuration parameters.
        configuration = nft_storage.Configuration(
            host = "https://api.nft.storage"
        )

        configuration = nft_storage.Configuration(
        access_token = apikey
    )
        with nft_storage.ApiClient(configuration) as api_client:
        # Create an instance of the API class
            api_instance = nft_storage_api.NFTStorageAPI(api_client)
            body = open(file, 'rb') # file_type | 

            # example passing only required values which don't have defaults set
            try:
                # Store a file
                api_response = api_instance.store(body, _check_return_type=False)
                return(api_response)
            except nft_storage.ApiException as e:
                return("Exception when calling NFTStorageAPI->store: %s\n" % e)


    def status_nft_storage(apikey,cid_):
        configuration = nft_storage.Configuration(
        host = "https://api.nft.storage"
    )
        configuration = nft_storage.Configuration(
            access_token = apikey
        )


        with nft_storage.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = nft_storage_api.NFTStorageAPI(api_client)
            cid = cid_ # str | CID for the NFT

            # example passing only required values which don't have defaults set
            try:
                # Get information for the stored file CID
                api_response = api_instance.status(cid,_check_return_type=False)
                return(api_response)
            except nft_storage.ApiException as e:
                return("Exception when calling NFTStorageAPI->status: %s\n" % e)

    def upload_web3_storage(apikey,file):

        body = open(file, 'rb')
        response = requests.post(
            "https://api.web3.storage/upload",
            headers={"Authorization": f'Bearer {apikey}'},
            files={"file": body}
        )

        return(response.json())

    def status_web3_storage(apikey,cid_):

        response = requests.get(f'https://api.web3.storage/status/{cid_}')
        return response.json()

    def nft_storage_download_link(cid_):
        data = f'https://nftstorage.link/ipfs/{cid_}'
        return data

    def web3_storage_download_link(cid_):
        data = f'https://{cid_}.ipfs.w3s.link/'
        return data

    
    def upload_pinata(pinata_api_key,pinata_secret_api_key, file):
        body = open(file, 'rb')
        pinata = PinataPy(pinata_api_key,pinata_secret_api_key)
        result = pinata.pin_file_to_ipfs(body)
        return result.json()