import os
import logging
import paramiko
import socket


LOCAL_FOLDER_CSV = 'tmp'
log = logging.getLogger(__name__)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_root = os.path.join('media')


class SFTPClient:
    """_summary_
    """
    def __init__(self, host, port, remote_path=None, local_path=None) -> None:
        """
        Initializes an instance of the SFTPClient class.

        Args:
            host (str): the hostname or IP address of the SFTP server.
            port (int): the port number to connect to.
            remote_path (str, optional): the remote path on the server. Defaults to "/upload".
            local_path (str, optional): the local path for downloaded files. Defaults to None.

        Raises:
            Exception: if host or port are not provided.
        """
        if not all([host, port]):
            raise Exception('Please Provide Correct Info')

        if local_path is None:
            self.local_path = os.path.join(base_dir, media_root, LOCAL_FOLDER_CSV)

        self.remote_path = remote_path

        if remote_path is None:
            self.remote_path = '/upload'
            self.remote_path += '/'

        self.host = socket.gethostbyname(host)
        self.port = port
        self.client = None
        self.connected = False

    def connect(self, username, password):
        """
        Connects to the SFTP server.

        Args:
            username (str): the username to authenticate with.
            password (str): the password to authenticate with.

        Returns:
            paramiko.SFTPClient: a client object for communicating with the SFTP server.
        """
        # Connect to the SFTP server
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=username, password=password)
        self.client = paramiko.SFTPClient.from_transport(transport)
        self.connected = True
        self.client.chdir(self.remote_path)

        print(f'Client connected.....Working on {self.remote_path}')

        return self.client

    def list_remote_files(self):
        """
        Lists the files in the remote directory.

        Returns:
            list: a list of filenames.
        """
        return self.client.listdir()

    def read_file(self, file_name):
        """
        Reads a file from the remote directory.

        Args:
            file_name (str): the name of the file to read.

        Returns:
            bytes: the contents of the file.
        """
        return self.client.file(file_name, mode='rb').read()

    def write_file(self, file_name, data):
        """
        Writes a file to the remote directory.

        Args:
            file_name (str): the name of the file to write.
            data (bytes): the contents of the file.

        Returns:
            str: the name of the uploaded file.
        """
        self.client.file(file_name, mode='wb').write(data)
        return file_name

    # Download a file from the server
    def download(self, file_name):
        """
        Downloads a file from the remote directory.

        Args:
            file_name (str): the name of the file to download.

        Returns:
            str: the local path of the downloaded file.
        """
        local_file_path = os.path.join(self.local_path, file_name)

        self.client.get(file_name, local_file_path)

        return local_file_path

    # Upload a file to the server
    def upload(self, file_name):
        """
        Uploads a file to the remote directory.

        Args:
            file_name (str): The name of the file to upload.

        Returns:
            str: The local file path.
        """
        local_file_path = os.path.join(self.local_path, file_name)
        self.client.put(local_file_path, file_name)

        return local_file_path

    def upload_delete_local(self, file_name):
        """
        Uploads a file to the remote directory, and deletes the local file.

        Args:
            file_name (str): The name of the file to upload.

        Returns:
            str: The local file path.
        """
        local_file_path = os.path.join(self.local_path, file_name)
        self.client.put(local_file_path, file_name)
        os.remove(local_file_path)

        return local_file_path

    def close_connection(self):
        """
        Closes the connection to the remote directory.
        """
        self.client.close()
        self.connected = False