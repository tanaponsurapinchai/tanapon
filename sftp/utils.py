import csv
from action import generate_csv_filename

def write_data_csv(sftp=None):
    """Write employee data to a CSV file.

    Args:
        sftp (SFTPClient, optional): An SFTP client object. Defaults to None.
    """
    mockup_data_employees_lists = [
        {"name": "John Doe", "age": 30, "title": "Software Engineer"},
        {"name": "Jane Smith", "age": 25, "title": "Data Scientist"},
        {"name": "Bob Johnson", "age": 40, "title": "Project Manager"},
    ]

    if sftp:
        filename = generate_csv_filename("employees")
        csvfile = sftp.client.file(filename, mode='w')
    else:
        filename = generate_csv_filename("employees")
        csvfile = open(filename, mode='w', newline="")

    header = list(mockup_data_employees_lists[0].keys())  # extract header from keys of first dict
    datas = []
    for employee in mockup_data_employees_lists:
        data = [employee[key] for key in header]  # extract data for each row
        datas.append(data)
    writer = csv.writer(csvfile, delimiter="|")
    writer.writerow(header)  # write header row
    writer.writerows(datas)  # write data rows

    if sftp:
        sftp.close_connection()
