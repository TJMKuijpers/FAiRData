import requests

class RetrieveDataCiteDOI:

    def __init__(self,doi_to_retrieve):
        self.DATACITEURL='https://api.datacite.org/dois/'
        self.doi=doi_to_retrieve

    def connect_to_url(self):
        response=requests.get(self.DATACITEURL)
        print("Response status code %d" % response.status_code)
        if response.status_code==200:
            print("Connected to DataCite API url")
            self.connection_established=True
        else:
            print("Cannot connect to DataCite API url")
            self.connection_established=False

    def retrieve_doi(self):
        if self.connection_established:
            response = requests.get(self.DATACITEURL+self.doi)
            if response.status_code==200:
                print(response.json())
            else:
                print('Status code %d: check DOI' % response.status_code)
        else:
            print('Connection is not established')