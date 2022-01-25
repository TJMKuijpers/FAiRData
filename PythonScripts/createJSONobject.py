##########################################################################
##################### Python script to create json file  #################
##########################################################################
# Author: T.J.M. Kuijpers

def create_json_object(data_set):
    index=0
    json_object=dict()
    for x in data_set.Key:
        json_object[x]=data_set.Value[index]
        index=index+1
    return json_object
