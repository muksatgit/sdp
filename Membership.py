'''class Membership:

    def __init__(self, file_name):
        self.file_name = file_name
        self.lines = []

    def read_lines(self):
        file = open(self.file_name)
        self.lines = file.readlines()
        file.close()
        self.lines = [line.strip() for line in self.lines[1:]]

'''

'''

example_file = open('/Users/muks/Scandic/File Zila/SF/Import/Membership/Membership.csv', 'r')
lines = example_file.readlines()
example_file.close()
lines = [line.strip() for line in lines[1:]]

for line in lines:
    member_data = line.split('|')
    MembershipId = member_data[8].replace('"', "")
    ExpiringPointsThisYear = member_data[11]

    if MembershipId == "30812310659463":
        print(f'{ExpiringPointsThisYear}')

'''