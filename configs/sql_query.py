__get_analytics_file = open("queries/getanalytics.sql", 'r')
get_analytics_query = __get_analytics_file.read()
__get_analytics_file.close()

__property_file = open("queries/getpropertylist.sql", 'r')
get_property_query = __property_file.read()
__property_file.close()