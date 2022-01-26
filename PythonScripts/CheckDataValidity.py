#####################################################################################################################
######################### Class to check data validity of xml DataCite Schema #######################################
#####################################################################################################################
# Author: T.J.M. Kuijpers   version 0.0.1 date (start) : 25 Januari 2022
import datetime
class CheckDataValidity:

    def __init__(self,Data=None,type=None):
        self.data=Data
        self.type=None
        self.SCHEMA='DataCite'
        self.DATEFORMART='d-%m-%Y'
        self.MANDATORYFIELDS=None
        self.na_checked=None
        self.required_fields = None
        self.correct_format = None

    def set_the_mandatory_fields(self) -> None:
        if self.type=='Administrative':
            self.MANDATORYFIELDS=['Creator','Title','Publisher','PublicationYear','ResourceType']
        if self.type=='Descriptive':
            self.MANDATORYFIELDS=['Title','Publisher','Publication year','Lead author','Principle investigator','Date','Abstract']
        if self.type='Structural':
            self.MANDATORYFIELDS=['Experiment','']
        print('Mandatory fields are set to match the %s metadata' % self.type)

    def check_for_na(self) -> None:
        # returns a boolean
        na_present=not all(self.data.values())
        if na_present:
            self.na_checked='Passed'
        else:
            self.na_checked='Failed'
        return None

    def check_format_of_date(self)-> None:
        try:
            datetime.datetime.strptime(self.data.Date, format)
        except ValueError:
            self.correct_format='Failed, format is wrong'
        except AttributeError:
            self.correct_format='Failed, json object has no data attribute'
        else:
            self.correct_format='Passed'
        return None

    def check_required_fields(self) -> None:
        print('Checking the required fields...')
        test_passed=0
        for x in self.MANDATORYFIELDS:
            field_present=x in self.data.keys()
            if field_present == False:
                # Raise an error warning without stopping the pyhton script
                print('Warning: metadata field %s is missing ! ' % x)
            else:
                test_passed=test_passed+1
        if test_passed == self.data.keys().__len__():
            self.required_fields='Passed'
        else:
            self.required_fields='Failed'
        return None
