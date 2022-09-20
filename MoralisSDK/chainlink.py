from colorama import Cursor
import requests
import sqlite3



class Chainlink:
    def __init__(self):
        pass
    
    def db_connect(self):
        sqliteConnection = sqlite3.connect('chainlink.db')
        cursor = sqliteConnection.cursor()
        return cursor

    def active_feeds(self,limit):
        cursor = self.db_connect()
        query = f'select * from Chainlink_Active_Feeds limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def Active_Feeds_Requesters(self,limit):
        cursor = self.db_connect()
        query = f'select * from Chainlink_Active_Feeds_Requesters limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def Keepers_BSC_Daily(self,limit):
        cursor = self.db_connect()
        query = f'select * from Chainlink_Keepers_BSC_Daily limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data

    def Keepers_ETH_Daily(self,limit):
        cursor = self.db_connect()
        query = f'select * from Chainlink_Keepers_ETH_Daily limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def Keepers_POLYGON_Daily(self,limit):
        cursor = self.db_connect()
        query = f'select * from Chainlink_Keepers_POLYGON_Daily limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def Oracle_Requests_over_Time(self,limit):
        cursor = self.db_connect()
        query = f'select * from Chainlink_Oracle_Requests_over_Time limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def Total_LINK_on_centralized_exchanges(self,limit):
        cursor = self.db_connect()
        query = f'select * from Total_LINK_on_centralized_exchanges limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data

    def chainlink_VRF_v1_daily_BSC(self,limit):
        cursor = self.db_connect()
        query = f'select * from chainlink_VRF_v1_daily_BSC limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def chainlink_VRF_v1_daily_ETH(self,limit):
        cursor = self.db_connect()
        query = f'select * from chainlink_VRF_v1_daily_ETH limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def chainlink_VRF_v1_daily_POLYGON(self,limit):
        cursor = self.db_connect()
        query = f'select * from chainlink_VRF_v1_daily_POLYGON limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def chainlink_VRF_v2_daily_BSC(self,limit):
        cursor = self.db_connect()
        query = f'select * from chainlink_VRF_v2_daily_BSC limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def chainlink_VRF_v2_daily_ETH(self,limit):
        cursor = self.db_connect()
        query = f'select * from chainlink_VRF_v2_daily_ETH limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def chainlink_VRF_v2_daily_POLYGON(self,limit):
        cursor = self.db_connect()
        query = f'select * from chainlink_VRF_v2_daily_POLYGON limit {limit}'
        data = cursor.execute(query)
        data = cursor.fetchall()
        return data


    


    

