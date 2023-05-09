import datetime
from dateutil import relativedelta
test_case = [
    {
        'start_date':datetime.date(2023, 4, 1),
        'end_date':datetime.date(2024, 3, 31)
    },
    {
        'start_date':datetime.date(2023, 4, 23),
        'end_date':datetime.date(2023, 9, 30)
    },
    {
        'start_date':datetime.date(2023, 3, 15),
        'end_date':datetime.date(2024, 3, 31)
    },
    {
        'start_date':datetime.date(2023, 4, 15),
        'end_date':datetime.date(2023, 4, 14)
    },
    {
        'start_date':datetime.date(2023, 4, 1),
        'end_date':datetime.date(2025, 3, 31)
    },
    {
        'start_date':datetime.date(2023, 3, 15),
        'end_date':datetime.date(2025, 3, 25)
    },
    {
        'start_date':datetime.date(2023, 11, 15),
        'end_date':datetime.date(2024, 5, 14)
    },
    {
        'start_date':datetime.date(2023, 4, 11),
        'end_date':datetime.date(2023, 4, 14)
    },
    {
        'start_date':datetime.date(2023, 3, 15),
        'end_date':datetime.date(2024, 4, 5)
    },
    {
        'start_date':datetime.date(2023, 4, 15),
        'end_date':datetime.date(2024, 10, 14)
    },
    {
        'start_date':datetime.date(2023, 4, 11),
        'end_date':datetime.date(2024, 10, 14)
    },
    {
        'start_date':datetime.date(2023, 4, 18),
        'end_date':datetime.date(2024, 3, 31)
    },    
]

def calculate_date_difference(obj:datetime):
    """Ex. output
    Test case 1:
    start_date:2023-04-01 end_date:2024-03-31 :: 0 ปี 11 เดือน 30วัน
    -------------------------------------
    Test case 2:
    start_date:2023-04-23 end_date:2023-09-30 :: 0 ปี 5 เดือน 7วัน
    -------------------------------------
    Test case 3:
    start_date:2023-03-15 end_date:2024-03-31 :: 1 ปี 0 เดือน 16วัน
    -------------------------------------
    Test case 4:
    start_date:2023-04-15 end_date:2023-04-14 :: 0 ปี 0 เดือน 0วัน
    -------------------------------------
    Test case 5:
    start_date:2023-04-01 end_date:2025-03-31 :: 1 ปี 11 เดือน 30วัน
    -------------------------------------
    Test case 6:
    start_date:2023-03-15 end_date:2025-03-25 :: 2 ปี 0 เดือน 10วัน
    -------------------------------------
    Test case 7:
    start_date:2023-11-15 end_date:2024-05-14 :: 0 ปี 5 เดือน 29วัน
    -------------------------------------
    Test case 8:
    start_date:2023-04-11 end_date:2023-04-14 :: 0 ปี 0 เดือน 3วัน
    -------------------------------------
    Test case 9:
    start_date:2023-03-15 end_date:2024-04-05 :: 1 ปี 0 เดือน 21วัน
    -------------------------------------
    Test case 10:
    start_date:2023-04-15 end_date:2024-10-14 :: 1 ปี 5 เดือน 29วัน
    -------------------------------------
    Test case 11:
    start_date:2023-04-11 end_date:2024-10-14 :: 1 ปี 6 เดือน 3วัน
    -------------------------------------
    Test case 12:
    start_date:2023-04-18 end_date:2024-03-31 :: 0 ปี 11 เดือน 13วัน
    -------------------------------------

    Args:
        obj (datetime): datetime.date()

    Returns:
        string: _years_ ปี _month_ เดือน _day_วัน
    """
    start_date = obj['start_date']
    end_date = obj['end_date']

    dif = relativedelta.relativedelta(end_date, start_date)

    return print(f'start_date:{start_date} end_date:{end_date} :: {dif.years} ปี {dif.months} เดือน {max(0, dif.days)}วัน')

# for run function
for i, obj in enumerate(test_case):
    print(f'Test case {i+1}:')
    calculate_date_difference(obj)
    print('-------------------------------------')

