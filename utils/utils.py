from datetime import datetime
from utils.prop import Prop


class Utils(object):

    def __init__(self):
        self.prop = Prop()



    @staticmethod
    def current_time():
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    @staticmethod
    def log(message) -> None:
        print(message)

