from owslib.wcs import WebCoverageService


class AvgTemperatureColorInfo:

    

    def __init__(self, wcs_link):
        self.my_wcs = WebCoverageService(wcs_link, version='2.0.1')
        
    
    def getMetaData(self):
        for item in dir(self.my_wcs.contents['AvgTemperatureColor']):
            if "_" not in item:
                print(item)

    def getGridInfo(self):
        for item in dir(self.my_wcs.contents['AvgTemperatureColor'].grid):
            if "_" not in item:
                print (item + ": " + str(self.my_wcs.contents['AvgTemperatureColor'].grid.__dict__[item]))

    def getSupportedFormat(self):
       print(self.my_wcs.contents['AvgTemperatureColor'].supportedFormats)

    def getTimePositions(self):
        time_positions = self.my_wcs.contents['AvgTemperatureColor'].timepositions
    
        # Check if timepositions is not None
        if time_positions is not None:
            # Iterate over the first 10 time positions and print them
            for time in time_positions[:10]:
                print(time.isoformat())
        else:
            print("Time positions are None.")