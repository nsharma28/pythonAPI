select * from dbt_source.fn_getPropertyList(%(p_city)s, %(p_state)s, %(p_proptype)s, %(p_minprice)s, %(p_maxprice)s, %(p_numbedrooms)s, %(p_numbathrooms)s, %(p_propsubtype)s, %(p_sqfoot)s, %(p_numstories)s, %(p_minyear)s, %(p_maxyear)s, %(p_mls)s, %(p_listingstatus)s, %(p_viewtype)s, %(p_lotsize)s, %(p_listingtype)s, %(p_garagespace)s, %(p_lat)s, %(p_lon)s);