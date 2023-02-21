from datetime import datetime

dateTest = '2023-02-04'
dataList = []
dataMonthNow = []

for x in range(1, 10):
    dataList.append(['Andhika', f'2023-02-0{x} 16:00:00', f'{x}', 'I'])
    
for i in dataList:
    dateFinger = datetime.strptime(i[1], '%Y-%m-%d %H:%M:%S').date()
    date_test = datetime.strptime(dateTest, '%Y-%m-%d').date()
    if dateFinger >= date_test:
        print(i)