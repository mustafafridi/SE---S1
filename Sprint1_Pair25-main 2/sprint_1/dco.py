from dbc import Dbc 

class Dco():
    def __init__(self, dc_connection):
        self.dc_connection = dc_connection


    def getMainAvgTempColor(self,Lat,Lon):
        wcps_query = f'''for $c in (AvgTemperatureColor) return encode($c[ ansi("2015-03-01T00:00:00":"2015-07-01T00:00:00"),Lat({Lat}), Lon({Lon})],"csv")'''
        self.dc_connection.execute_query_csv(wcps_query)

    def getMinTempColor(self,Lat,Lon):
        wcps_query = f'for $c in (AvgTemperatureColor) return encode(min($c[Lat({Lat}), Lon({Lon}), ansi("2015-03-01T00:00:00":"2015-07-01T00:00:00")]), "csv")'
        self.dc_connection.execute_query_print(wcps_query)

    def getMaxTempColor(self,Lat,Lon):
        wcps_query = f'for $c in (AvgTemperatureColor) return encode(max($c[Lat({Lat}), Lon({Lon}), ansi("2015-03-01T00:00:00":"2015-07-01T00:00:00")]), "csv")'
        self.dc_connection.execute_query_print(wcps_query)

    def getAverageAvgTempColor(self,Lat,Lon):
        wcps_query = f'for $c in (AvgTemperatureColor) return encode(avg($c[Lat({Lat}), Lon({Lon}), ansi("2015-03-01T00:00:00":"2015-07-01T00:00:00")]), "csv")'
        self.dc_connection.execute_query_print(wcps_query)

    # def getAvgerageAvgTempColor(self, lat, long):
    #     wcps_query = f'''
    #     for $c in (AvgLandTemp)
    #     return
    #         avg($c[Lat({lat}), Long({long}), ansi("2014-01":"2014-12")])
    #     '''
    #     return self.execute_query(wcps_query)