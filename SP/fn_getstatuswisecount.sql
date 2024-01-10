-- FUNCTION: recolorado.fn_getstatuswisecount()

-- DROP FUNCTION IF EXISTS recolorado.fn_getstatuswisecount();

CREATE OR REPLACE FUNCTION recolorado.fn_getstatuswisecount(
	)
    RETURNS TABLE(count integer, status character varying) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$

 
DECLARE 	
	 table2query text;
     sqlquery text;
     
 BEGIN 	
	
    
	-- select * from recolorado.fn_getstatuswisecount();
    
	
	    RETURN QUERY
		Select Count(*)::int,p.status from recolorado.property_ptnf p group by p.status;
 
END;  

$BODY$;

ALTER FUNCTION recolorado.fn_getstatuswisecount()
    
