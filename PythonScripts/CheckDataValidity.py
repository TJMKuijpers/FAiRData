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
        except AttributeError:
            print('Object has no date attribute')
            correct_format=False
        else:
            correct_format=True
        return correct_format

    def check_required_fields(self):
        for x in self.MANDATORYFIELDS:
            field_present=x in self.data.keys()
            if field_present == False:
                # Raise an error warning without stopping the pyhton script
                print('Warning: metadata field %s is missing ! ' % x)
            else:
                print('All is fine')
        return None # return None since we only raise errors if a field is not present

