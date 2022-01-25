#####################################################################################################################
######################### Class to check data validity of xml DataCite Schema #######################################
#####################################################################################################################
# Author: T.J.M. Kuijpers   version 0.0.1 date (start) : 25 Januari 2022

class CheckDataValidity:

    def __init__(self,Data=None):
        self.data=Data
        self.SCHEMA='DataCite'
        # TODO find the format for strings and dates in DataCite schema
        self.AUTHORFORMART=''
        self.DATAFORMAR=''
        self.FIELDS=['Author','Date','Title']

    def check_for_na(self):
        # returns a boolean
        na_present=self.data.isna().any()
        return na_present

    def check_format_of_cells(self):
        # Function to check if values have the right format
        return None

    def check_fields_study_meta(self):
        for x in self.FIELDS:
            field_present=x in self.data.keys()
            if field_present == False:
                # Raise an error warning without stopping the pyhton script
                print('Warning: metadata field %d is missing ! ' % x)
            else:
                # keep track if the number of trues is equal to the self.FIELDS length
                # TODO: add the tracker for true
        return None # return None since we only raise errors if a field is not present

