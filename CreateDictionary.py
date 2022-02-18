def create_dictionary(title_input,creator_input,subject_input,description_input,publisher_input,contributor_input,date_input,type_input,format_input,identifier_input,source_input,language_input,relation_input,coverage_input,rights_input):
    # create a dictionary with the input
    dict_dc={
    'title':title_input,
    'creater':creator_input,
    'subject':subject_input,
    'description':description_input,
    'publisher':publisher_input,
    'contributor':contributor_input,
    'date':date_input,
    'type':type_input,
    'format':format_input,
    'identifier':identifier_input,
    'source':source_input,
    'language':language_input,
    'relation':relation_input,
    'coverage':coverage_input,
    'rights':rights_input
    }
    return dict_dc

def create_dc_dictionary(dictionary_input):
    {f'dc:{k}': v for k, v in dictionary_input.items()}
    return dictionary_input