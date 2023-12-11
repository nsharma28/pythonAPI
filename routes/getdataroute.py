from fastapi import Request, Response
import json
from fastapi_utils.inferring_router import InferringRouter
import os
from models.samplemodel import *
from service.dataservice import DataService
from common.Response import *



router = InferringRouter(prefix="/data")


class CityRouter:
    @router.post("/getPropertyList",tags=["raw/data"])
    async def get(request:Request, propertyListReqModel:getPropertyListReq):
            try:
                return Response.data(DataService.getpropertyList(propertyListReqModel))
            except Exception as ex:
                return Response.error(ex)
            
    @router.post("/getAnalytics",tags=["raw/data"])
    async def insertsample(request:Request,analyticsReqModel:getAnalyticsReq):
            try:
                return Response.data(DataService.getAnalytic(analyticsReqModel))
            except Exception as ex:
                return Response.error(ex)
