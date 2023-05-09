import datetime


def generate_csv_filename(prefix: str, file_type: str = 'csv') -> str:
    """
    Generate a CSV filename with the specified prefix and the current local date in the format YYYY-MM-DD.

    Args:
        prefix (str): A string to prepend to the filename.
        file_type (str, optional): The file extension. Defaults to 'csv'.

    Returns:
        str: The generated filename in the format '{prefix}_{YYYY-MM-DD}.{file_type}'.
    """
    local_time = datetime.datetime.now().strftime('%Y-%m-%d')
    return f'{prefix}_{local_time}.{file_type}'