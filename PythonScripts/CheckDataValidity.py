#####################################################################################################################
######################### Class to check data validity of xml DataCite Schema #######################################
#####################################################################################################################
# Author: T.J.M. Kuijpers   version 0.0.1 date (start) : 25 Januari 2022
import datetime
class CheckDataValidity:

    def __init__(self,Data=None):
        self.data=Data
        self.SCHEMA='DataCite'
        self.DATEFORMART='d-%m-%Y'
        self.MANDATORYFIELDS=['Identifier','Creator','Title','Publisher','PublicationYear','ResourceType']

    def check_for_na(self) -> bool:
        # returns a boolean
        na_present=self.data.isnull().values.any()
        return na_present

    def check_format_of_date(self)-> bool:
        try:
            datetime.datetime.strptime(self.data.Date, format)
        except ValueError:
            correct_format=False
        else:
            correct_format=True
        return correct_format

    def check_required_fields(self):
        for x in self.FIELDS:
            field_present=x in self.data.keys()
            if field_present == False:
                # Raise an error warning without stopping the pyhton script
                print('Warning: metadata field %d is missing ! ' % x)
            else:
                # keep track if the number of trues is equal to the self.FIELDS length
                # TODO: add the tracker for true
        return None # return None since we only raise errors if a field is not present

