
from common.rdb_dal.sql_utility.sql_utility import SqlUtility
from common.rdb_dal.exception.common_exceptions import OpenConnectionError

# Library Import
import psycopg2
from psycopg2 import extras
from urllib.parse import urlparse

class PostgresSql(SqlUtility):
    

    def __init__(self,connection_string):
        """ Default contractor will be called to instantiate the defined variable.

        Args:
            database (string): DataBase Name
            user (string): User Name
            password (string): Password
            host (string): Host
            port (string): Port
            
        """
        pg_params = urlparse(connection_string)
        super().__init__(provider = "postgresDB")
        self.database = pg_params.hostname
        self.user = pg_params.username
        self.host = pg_params.scheme
        self.port = pg_params.port
        self.password = pg_params.password
    
    def open_connection(self):
        """ Create the sources connection 

        Raises:
            OpenConnectionError: Raise when connection is not established or giving error due to any reasons

        Returns:
            [Object]: sources connection object
            
        """
        connection = psycopg2.connect(database = self.database, user = self.user , password = self.password, host = self.host, port = self.port) #getting postgres connection
        #connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE)

        return connection

    def execute_batch_insert(self,connection_obj,query, data_model):
        """ Execute batch insert

        Raises:
            OpenConnectionError: Raise when connection is not established or giving error due to any reasons

        Returns:
            [Object]: sources connection object
            
        """
        
        return extras.execute_batch(connection_obj.cursor(),query,data_model)
        

    
            




