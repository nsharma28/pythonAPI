-- FUNCTION: recolorado.fn_getpropertydetail(text)

-- DROP FUNCTION IF EXISTS recolorado.fn_getpropertydetail(text);

CREATE OR REPLACE FUNCTION recolorado.fn_getpropertydetail(
	p_bfcid bigint)
    RETURNS json
    as $$

 -- select * from recolorado.fn_getpropertydetail(18532035560088) as result
 
 
DECLARE 	
	 table2query text;
     sqlquery text;
	 dataresult json;
	 property_json json;
	 media_json json;
     
 BEGIN 	
	
				select json_agg(property_data) from (
				select
					p.*,
					f.*,
					u.user_sourceid,
					u.office_name
				from recolorado.property_ptnf p
				inner join recolorado.features_ptnf f on p.bfcid = f.bfcid
				inner join recolorado.user_ptnf u on p.bfcid = u.bfcid
				where p.bfcid = p_bfcid ) property_data
				into property_json;
				
				select json_agg(media_data) from (
				select 
					m.*
				from recolorado.media_ptnf m
				where m.bfcid = p_bfcid) media_data
				into media_json;
	
				SELECT json_build_object(
					'property', json_agg(property_json),
					'media', json_agg(media_json)
				) INTO dataresult;
		
				
	       return dataresult;
	
END;  

$$ language plpgsql;

ALTER FUNCTION recolorado.fn_getpropertydetail(bigint)
    OWNER TO mlsuser;
