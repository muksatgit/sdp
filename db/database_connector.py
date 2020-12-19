import mysql.connector
from utils.prop import Prop
from utils.utils import Utils
from app_constants import AppConst


class DBConnector:

    def __init__(self):
        self.connection = None
        self.prop = Prop()

    def __enter__(self):
        self.connection = mysql.connector.connect(
            user=self.prop.get_prop(AppConst.DB_USER),
            password=self.prop.get_prop(AppConst.DB_PASSWORD),
            host=self.prop.get_prop(AppConst.DB_HOST),
            port=self.prop.get_prop(AppConst.DB_PORT),
            database=self.prop.get_prop(AppConst.DB_NAME),
            auth_plugin='mysql_native_password')
        Utils.log("DB Connected sucessfully")
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.disconnect()