class CreateXMLFile:

    def __init__(self, data_for_xml=None):
        self.data = data_for_xml
        self.xml_object = None
        self.test_result=None

    def convert_json_to_xml(self) -> None:
        xml_object = None
        self.xml_object = xml_object
        return None

    def text_xml(self,xml) -> bool:
        # test
        test = True
        return test

    def validate_xml_correct(self) -> None:
        test_result = self.test_xml(self.xml_object)
        if test_result:
            print('XML format is correct')
        else:
            print('XML format is not correct')
        self.test_result = test_result
        return None

    def write_xml_object(self) -> None:
        if self.test_result:
            print('XML written to folder')
        else:
            return None

