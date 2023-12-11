from datetime import datetime
import time
from models.samplemodel import *
from common.rdb_dal.sql import Sql
from configs import sql_query
from common.MyConvert import *
from common.config_param import config_dict
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from common.logs.log import *



class DataService:
    data_folder = ''
    field_mapping_flags = ''
    
    def getpropertyList(propertyListReqModel:getPropertyListReq())->list[getPropertyListRes]:
        sql = Sql('default')
        return sql.execute_list(getPropertyListRes,sql_query.get_property_query, MyConvert.to_dict(propertyListReqModel))
    
    def getAnalytic(analyticsReqModel:getAnalyticsReq())->list[getAnalyticsRes]:
        sql = Sql('default')
        return sql.execute_list(getAnalyticsRes,sql_query.get_analytics_query, MyConvert.to_dict(analyticsReqModel))
    