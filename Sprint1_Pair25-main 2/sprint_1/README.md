Web Coverage Service (WCS) Client

This program interacts with a remote Web Coverage Service (WCS) server to retrieve temperature-related data for specific geographical locations.

Components:

1. Dbc Class: Responsible for connecting to the WCS server and executing queries. Utilizes the `requests` library for HTTP communication.

2. Dco Class: Encapsulates methods for querying temperature-related data from the WCS server. Constructs WCPS queries based on latitude and longitude coordinates.

3. AvgTemperatureColorInfo Class: Provides metadata and information about the 'AvgTemperatureColor' coverage. Methods retrieve general metadata, grid information, supported formats, and time positions.

4. Main.ipynb: Jupyter Notebook serving as the entry point. Initializes connections, demonstrates Dco class usage, and queries temperature data.

Documentation:

- Dbc Class:
  - __init__(self, wcs_server): Initializes with WCS server URL.
  - execute_query_csv(self, query): Executes a WCPS query and saves CSV data to 'output.csv'.
  - execute_query_print(self, query): Executes a WCPS query and prints content.

- Dco Class:
  - __init__(self, dc_connection): Initializes with Dbc connection.
  - Methods:
    - getMainAvgTempColor(self, Lat, Lon)
    - getMinTempColor(self, Lat, Lon)
    - getMaxTempColor(self, Lat, Lon)
    - getAverageAvgTempColor(self, Lat, Lon)

Usage:

Instantiate Dbc, initialize connection to WCS server.
Instantiate Dco with Dbc connection.
Invoke Dco methods with latitude and longitude coordinates.

Testing:

Two test files (`test_dbc.py`, `test_dco.py`) utilize the `unittest` framework for testing Dbc and Dco classes.
