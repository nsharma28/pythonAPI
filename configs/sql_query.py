__get_analytics_file = open("queries/getanalytics.sql", 'r')
get_analytics_query = __get_analytics_file.read()
__get_analytics_file.close()

__property_file = open("queries/getpropertylist.sql", 'r')
get_property_query = __property_file.read()
__property_file.close()

__property_detail_file = open("queries/getpropertydetail.sql", 'r')
get_property_detail_query = __property_detail_file.read()
__property_detail_file.close()

_active_vs_sold_file = open("queries/getactivevssold.sql", "r")
get_active_vs_sold_query = _active_vs_sold_file.read()
_active_vs_sold_file.close()

_status_wise_count_file = open("queries/getstatuswisecount.sql","r")
get_status_wise_count_query = _status_wise_count_file.read()
_status_wise_count_file.close()     
