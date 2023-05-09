from client import SFTPClient
from utils import write_data_csv
from dotenv import load_dotenv
import os
import sys
sys.setrecursionlimit(2000) # Set the maximum nested function level to 2000

load_dotenv()

sftp_host = os.getenv('SFTP_HOST')
sftp_port = int(os.getenv('SFTP_PORT'))
sftp_user = os.getenv('SFTP_USERNAME')
sftp_password = os.getenv('SFTP_PASSWORD')

def sftp_export_data():
    """
    Uploads employee data to an SFTP server using an SFTP client.

    Args:
        host (str): The SFTP server host address.
        port (int): The SFTP server port.
        username (str): The SFTP server username.
        password (str): The SFTP server password.
    """
    client = SFTPClient(host=sftp_host, port=sftp_port)
    client.connect(username=sftp_user, password=sftp_password)
    print('Uploading employee data to codium sftp...\n')

    write_data_csv(sftp=client)

    client.close_connection()
    print('SFTP Employee Success')

sftp_export_data()