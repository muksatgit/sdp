import mysql.connector


class DBConnector:

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(user='python', password='Aladin@123',
                                     host='localhost',
                                     port='3306',
                                     database='gft_reports',
                                     auth_plugin='mysql_native_password')
        print('DB Connected..')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.disconnect()






'''

def connect_to_db():
    db = mysql.connector.connect(user='python', password='Aladin@123',
                              host='muks.local',
                              port='3306',
                              database='MDB',
                              auth_plugin='mysql_native_password')


def read_insert_data():
    with open('/Users/muks/Scandic/PyCharm/sdp/res/GFT_Power_BI.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=', ')
        for row in csv_reader:
            print(row)


read_insert_data()


'''




'''

query = "SELECT * FROM movies"
cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)

db.close()
'''