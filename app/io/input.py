import pandas


def text_fr_console():
    """
    Function for reading from console.

    Returns:
        str: The text that was read from console.
    """
    return input("Enter text: ")


def text_fr_file(file_path):
    """
    Function for reading from file.

    Args:
        file_path (str): path to file where we read text

    Returns:
        str: The text that was read from file.
    """
    try:
        with open(file_path, 'r') as file:
            t = file.read()
            print(f"Text was read from {file_path}")
            return t
    except FileNotFoundError:
        print("The file wasn't found")
        return None


def text_fr_file_pandas(file_path):
    """
    Function for reading from file using pandas library.

    Args:
        file_path (str): path to file where we read text

    Returns:
        str: The text that was read from file.
    """

    try:
        data = pandas.read_csv(file_path, header=None)
        return ' '.join(data[0].tolist())
    except FileNotFoundError:
        print("The file wasn't found")
