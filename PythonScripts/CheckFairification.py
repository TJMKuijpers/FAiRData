import os
import chardet

class CheckFairificaiton:

    def __init__(self,file_name=None):
        self.class_name='Fair Check'
        self.FILENAME=file_name
        self.LOWSCOREEXTENSION=['.doc','.wpd','.dvi','.sid','.psd','.jpx','.jpf','.eps','.swf','.xls','.ppt']
        self.MEDIUMSCOREEXTENSION=['.css','.dtd','.rtf','.html','.sgml','.docx','.sxw','.odt']
        self.HIGHSCOREEXTENSION=['.xml','..jp2','.png','.svg','.csv','.sql']
        self.SPECIALCASES=['.txt','.pdf','.tiff']  # special cases because of encoding
        self.ENCODINGHIGHFAIRNESS=['UTF-8','UTF-16','USASCII']
        self.ENCODINGMEDIUMFAIRNESS=['ISO 8859-1']

    def fairness_of_txt(self) -> str:
        with open(self.FILENAME,'rb') as rawdata:
            result_encoding=chardet.detect(rawdata.read())
        encoding=result_encoding['encoding']
        if encoding.isin(self.ENCODINGHIGHFAIRNESS):
            class_fairness='High'
        if encoding.isin(self.ENCODINGMEDIUMFAIRNESS):
            class_fairness='Medium'
        else:
            class_fairness='Low'
        return class_fairness


    def score_fairness_data_type(self) ->None:
        # Check the extension of the file
        # TODO: what if there is a medium fairness for one type of extension?
        filename, file_extension = os.path.splitext(self.FILENAME)
        if file_extension.isin(self.LOWSCOREEXTENSION):
            print('Low score on file extension')
        if file_extension.isin(self.HIGHSCOREEXTENSION):
            print('High score on file extension')
        if file_extension.isin(self.MEDIUMSCOREEXTENSION):
            print('Medium score on file exteions')
        if file_extension.isin(self.SPECIALCASES):
            if file_extension =='.txt':
                score=self.fairness_of_txt()
            if file_extension =='.pdf':
                print('Identifying pdf encoding is not yet supported')

        return None



