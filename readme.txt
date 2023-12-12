1) Open SP folder and run the SP in postgres of server using pgadmin installed in your laptop, remember to open mlsdb and then execute query.
    you can check the SP working right or not by executing below query: 
   select * from recolorado.fn_getpropertydetail(18532035560088) as result;
2) Zip the whole code and copy and paste into the server.
3) I have changed all configurations according to the server.
4) just go to the location where main.py file is there and enter the below command
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
5) This will run this API on port 8000, so type serverip:8000/docs this will open the fastapi UI 
6) You will find these three POST calls

POST
/data/getPropertyList

POST
/data/getAnalytics

POST
/data/getPropertyDetail
Getpropertydetail

7) Click on the down arrow, then click 'try it out'
   enter the required values in Request Body for eg; (Getpropertydetail call)
    {
      "pBfcid": 18532035560088
    }
    and click on execute.
