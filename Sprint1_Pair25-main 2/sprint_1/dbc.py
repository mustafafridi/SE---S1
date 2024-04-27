
import requests

class Dbc:
    def __init__(self, wcs_server):
        self.wcs_server = wcs_server
    
    def execute_query_csv(self, query):
        
        response = requests.post(self.wcs_server, data = {'query':query})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the CSV data to a file
            with open('output.csv', 'wb') as f:
                f.write(response.content)
            print('CSV file saved successfully.')
        else:
            # Print an error message if the request failed
            print('Error:', response.text)


    def execute_query_print(self, query):
        response = requests.post(self.wcs_server, data = {'query':query})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the CSV data to a file
            print(response.content)
        else:
            # Print an error message if the request failed
            print('Error:', response.text)