import datetime
from dateutil import relativedelta
test_case = [
    # {
    #     'start_date':datetime.date(2023, 4, 1),
    #     'end_date':datetime.date(2024, 3, 31)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 23),
    #     'end_date':datetime.date(2023, 9, 30)
    # },
    # {
    #     'start_date':datetime.date(2023, 3, 15),
    #     'end_date':datetime.date(2024, 3, 31)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 15),
    #     'end_date':datetime.date(2023, 4, 14)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 1),
    #     'end_date':datetime.date(2025, 3, 31)
    # },
    # {
    #     'start_date':datetime.date(2023, 3, 15),
    #     'end_date':datetime.date(2025, 3, 25)
    # },
    # {
    #     'start_date':datetime.date(2023, 11, 15),
    #     'end_date':datetime.date(2024, 5, 14)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 11),
    #     'end_date':datetime.date(2023, 4, 14)
    # },
    # {
    #     'start_date':datetime.date(2023, 3, 15),
    #     'end_date':datetime.date(2024, 4, 5)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 15),
    #     'end_date':datetime.date(2024, 10, 14)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 11),
    #     'end_date':datetime.date(2024, 10, 14)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 18),
    #     'end_date':datetime.date(2024, 3, 31)
    # },
    # {
    #     'start_date':datetime.date(2023, 4, 18),
    #     'end_date':datetime.date(2024, 3, 31)
    # },
    {
        'start_date':datetime.date(2023, 3, 1),
        'end_date':datetime.date(2024, 2, 29)
    },
    {
        'start_date':datetime.date(2023, 3, 1),
        'end_date':datetime.date(2024, 2, 28)
    },
    {
        'start_date':datetime.date(2023, 4, 18),
        'end_date':datetime.date(2024, 3, 31)
    },
    {
        'start_date':datetime.date(2023, 1, 1),
        'end_date':datetime.date(2023, 2, 28)
    },
    {
        'start_date':datetime.date(2023, 3, 15),
        'end_date':datetime.date(2024, 3, 31)
    },
]

def calculate_date_difference(obj: dict) -> str:
    """
    Args:
        obj (dict): a dictionary containing 'start_date' and 'end_date' keys with datetime.date values

    Returns:
        str: a string with the format '_years_ ปี _months_ เดือน _days_ วัน'
    """
    start_date = obj['start_date']
    end_date = obj['end_date']

    dif = relativedelta.relativedelta(end_date + datetime.timedelta(days=1), start_date)

    return f"{dif.years} ปี {dif.months} เดือน {max(dif.days, 0)} วัน"

# for run function
for i, obj in enumerate(test_case):
    print(f'Test case {i+1}:')
    print(calculate_date_difference(obj))
    print('-------------------------------------')

