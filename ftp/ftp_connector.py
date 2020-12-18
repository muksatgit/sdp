import pysftp
from app_constants import AppConst
from utils.utils import Utils
import csv


class FTPConnector:

    def __init__(self):
        self.cnopts = pysftp.CnOpts()
        self.cnopts.hostkeys = None

    def download_file(self,remote_file: str, local_file: str) -> None:
        with pysftp.Connection(host=AppConst.FTP_host_name, username=AppConst.FTP_USERNAME, password=AppConst.FTP_PASSWORD, cnopts=self.cnopts) as sftp:
            def __print_totals(transferred, toBeTransferred):
                progress = round(transferred * 100 / toBeTransferred)
                Utils.log(f'{progress} %')
            remote_file_path = remote_file#AppConst.SF_GFT_DATA_REMOTE_FILE
            local_file_path = local_file#AppConst.SF_GFT_DATA_LOCAL_FILE
            sftp.get(remote_file_path, local_file_path, callback=__print_totals)
            Utils.log(f'Download Completed for and file is at: {local_file}')









    def read_file(self):

        Utils.log(AppConst.SF_GFT_DATA_LOCAL_FILE)
        local_file = open(AppConst.SF_GFT_DATA_LOCAL_FILE, 'r', encoding='utf-16le')
        csv_data = csv.reader(local_file)
        lines = local_file.readlines()
        local_file.close()
        lines = [line.strip() for line in lines[1:]]

        for line in lines:
            member_data = line.split(',')
            SalesforceSubscriberID = member_data[0] #.replace('"', "")
            ConfirmationNumber = member_data[1]
            Utils.log(f'{SalesforceSubscriberID} -- {ConfirmationNumber}')