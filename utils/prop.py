from jproperties import Properties

class Prop(object):

    def __init__(self):
        self.root = '/Users/muks/Scandic/code/python_projects/sdp/'
        self.config = Properties()

        with open(f'{self.root}/app-config.properties', 'rb') as config_file:
            self.config.load(config_file)

    def get_prop(self, key:str) -> str :
        return self.config.get(key).data

