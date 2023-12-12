from typing import List
from pydantic import BaseModel
from fastapi_camelcase import CamelModel

class getPropertyDetailReq(CamelModel,BaseModel):
    p_bfcid:int = 0
    
class getPropertyDetailRes(CamelModel,BaseModel):
    result:dict = None

class getAnalyticsReq(CamelModel,BaseModel):
    p_city:str = None
    p_state:str = None
    p_proptype:str = None
    p_minprice:int = None
    p_maxprice:int = None
    p_numbedrooms:int = None
    p_numbathrooms:int = None
    
class getAnalyticsRes(CamelModel,BaseModel):
    avgsale:str = None
    avgdays:int = None
    numproperty:int = None
    
class getPropertyListRes(CamelModel,BaseModel):
    bfcid:int = None
    price:str = None
    beds:int = None
    bath:int =None
    photourl:str = None
    link:str = None
    lat:float = None
    lon:float = None
    sqft:int = None
    pintitle:str = None
    status:str = None
    mls_number_title:str = None
    datasource:str = None
    courtesy:str = None
    copyright:str = None
    vtour_url:str = None
    
class getPropertyListReq(CamelModel,BaseModel):
    p_city:str = ''
    p_state:str = ''
    p_proptype:str = ''
    p_minprice:int = None
    p_maxprice:int = None
    p_numbedrooms:int = None
    p_numbathrooms:int = None
    p_propsubtype:str = None
    p_sqfoot:int = None
    p_numstories:int = None
    p_minyear:int = None
    p_maxyear:int = None
    p_mls:str = None
    p_listingstatus:str = None
    p_viewtype:str = None
    p_lotsize:int = None
    p_listingtype:str = None
    p_garagespace:int = None
    p_lat:float = None
    p_lon:float = None
