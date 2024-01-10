-- FUNCTION: recolorado.fn_getactivevssold(text, text)

-- DROP FUNCTION IF EXISTS recolorado.fn_getactivevssold(text, text);

CREATE OR REPLACE FUNCTION recolorado.fn_getactivevssold(
	p_city text DEFAULT NULL::text,
	p_state text DEFAULT NULL::text)
    RETURNS TABLE(count integer, status character varying, year integer, month integer) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$

 
DECLARE 	
	 table2query text;
     sqlquery text;
     
 BEGIN 	
	
    -- select * from recolorado.fn_getactivevssold('Denver','CO');
	-- select * from recolorado.fn_getactivevssold('Denver','CO');
    
	
	    RETURN QUERY
		select
			count(*)::int as count,
			a.status,
			a.prop_year::int,
			a.prop_month::int
		from (
			select
				p.status,
				EXTRACT(YEAR FROM p.listdate) as prop_year,
				EXTRACT(MONTH FROM p.listdate) as prop_month
			from recolorado.property_ptnf p
			where p.status IN ('Active', 'Price Change', 'Extended', 'New', 'Under Agreement', 'Reactivated', 'Back on Market', 'Pending') 
			and 
			case
				when (p_state is not null) then p.state = any(string_to_array(p_state,',')::character varying[])
				else true
			end and 
			case
				when (p_city is not null) then p.city = any(string_to_array(p_city,',')::character varying[])
				else true
			end
		) a 
		group by a.status, a.prop_month, a.prop_year
		order by a.status,a.prop_year, a.prop_month;
 
END;  

$BODY$;

ALTER FUNCTION recolorado.fn_getactivevssold(text, text)

