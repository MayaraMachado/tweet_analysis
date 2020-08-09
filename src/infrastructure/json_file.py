import json

class JsonFile():

    def __init__(self):
        self.filepath = '/files'

    def __prepare_date(self, data):
        pass

    def write_file(self, name_file, data, encoding='utf8'):
        '''
        '''

        with open(self.filepath+'/'+name_file, 'a', encoding=encoding) as filename:

            for item in data:
                
                # convert to string
                json_str = json.dumps(data._json)

                # deserialize string to an python dict
                parsed = json.load(json_str)

                # write file
                json.dump(parsed, filename, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))



