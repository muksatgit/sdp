from ftp.ftp_connector import FTPConnector
from db.database_connector import DBConnector
from app_constants import AppConst
from utils.utils import Utils

import csv


class AppController(object):

    def __init__(self):
        self.f_connector = FTPConnector()
        self.util = Utils()

    def load_gft_data_from_ftp(self) -> None:

        _remote_file = self.util.prop.get_prop(AppConst.SF_GFT_DATA_REMOTE_FILE)
        _local_file = self.util.prop.get_prop(AppConst.SF_GFT_DATA_LOCAL_FILE)

        self.f_connector.download_file(remote_file=_remote_file, local_file=_local_file)

    def load_scorpio_profile_from_ftp(self) -> None:
        _remote_file = self.util.prop.get_prop(AppConst.SCORPIO_PROFILE_REMOTE_FILE)
        _local_file = self.util.prop.get_prop(AppConst.SCORPIO_PROFILE_LOCAL_FILE)

        self.f_connector.download_file(remote_file=_remote_file, local_file=_local_file)

    def read_data_from_db(self) -> None :
        with DBConnector() as db_connector:
            my_cursor = db_connector.cursor()
            my_query = 'SELECT * FROM sf_import'
            my_cursor.execute(my_query)
            records = my_cursor.fetchall()
            for record in records:
                print(record)

    def read_gft_csv_inset_to_db(self) -> None:
        _file_name = self.util.prop.get_prop(AppConst.SF_GFT_DATA_LOCAL_FILE)
        local_file = open(_file_name, 'r', encoding='utf-16le')
        csv_data = csv.reader(local_file)
        next(csv_data, None)
        start = Utils.current_time()
        print(start)

        with DBConnector() as db_connector:
            my_cursor = db_connector.cursor()
            query = """INSERT INTO sf_import(SalesforceSubscriberID,ConfirmationNumber,Date,HotelCountry,ResortCode,NameID,Channel) VALUES( %s, %s, %s, %s, %s, %s, %s)"""
            for line in csv_data:
                my_cursor.execute(query, line)
                db_connector.commit()
            my_cursor.close()
        local_file.close()
        end = Utils.current_time()
        print(end)
        print('\n')
        print(int(end)-int(start))

    def read_profile_csv_inset_to_db(self) -> None:
        _file_name = self.util.prop.get_prop(AppConst.SCORPIO_PROFILE_LOCAL_FILE)
        local_file = open(_file_name, 'r')
        csv_data = csv.reader(local_file, delimiter='|')
        next(csv_data, None)
        start = Utils.current_time()
        Utils.log(start)
        with DBConnector() as db_connector:
            my_cursor = db_connector.cursor()
            query = """INSERT INTO profile(NameId,Title,FirstName,LastName,Gender,BirthDate,Language,RicaKeyword,RicaKeywordType,PrimaryEmailAddress,PrimaryMobileNumber,Address1,Address2,City,ZipCode,Country,AddressType,ThirdPartyYn,EmailYn,ActiveYn) VALUES( %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"""
            i = 0
            for line in csv_data:
                my_cursor.execute(query, line)
                db_connector.commit()
                i = i+1
                Utils.log(f'{i}')
            my_cursor.close()
        local_file.close()
        end = Utils.current_time()
        Utils.log(end)

    def read_res_txt_inset_to_db(self) -> None:
        _file_name = self.util.prop.get_prop(AppConst.SCORPIO_RES_LOCAL_FILE)
        local_file = open(_file_name, 'r')
        csv_data = csv.reader(local_file, delimiter='|')
        next(csv_data, None)
        start = Utils.current_time()
        Utils.log(start)
        with DBConnector() as db_connector:
            my_cursor = db_connector.cursor()
            query = """
            INSERT INTO reservation(first,last,email,language,phone_type,phone_no,country,title,name_id,resv_name_id,confirmation_no,confirmation_leg_no,trunc_begin_date,trunc_end_date,number_of_nights,adults,children,rate_code,room_type,channel,source_code,room_revenue_local,currency_code,resort,booking_status,promo_code,corporate_code,travel_agent_code,contracted_rate,booking_date,leadtime,promotion_code1,promotion_code2,promotion_code3,total_points,qualifying_nights,non_member,guarantee_code,market_code,block_code,birth_date,gender) VALUES( %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"""
            i = 0
            for line in csv_data:
                my_cursor.execute(query, line)
                db_connector.commit()
                i = i+1
                Utils.log(f'{i}')
            my_cursor.close()
        local_file.close()
        end = Utils.current_time()
        Utils.log(end)


