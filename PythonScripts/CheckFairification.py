import os

class CheckFairificaiton:

    def __init__(self,file_name=None):
        self.class_name='Fair Check'
        self.FILENAME=file_name
        self.LOWSCOREEXTENSION=[]
        self.HIGHSCOREEXTENSION=[]

    def score_fairness_data_type(self):
        # Check the extension of the file
        # TODO: what if there is a medium fairness for one type of extension?
        filename, file_extension = os.path.splitext(self.FILENAME)
        if file_extension.isin(self.LOWSCOREEXTENSION):
            print('Low score on file extension')
        if file_extension.isin(self.HIGHSCOREEXTENSION):
            print('High score on file extension')
