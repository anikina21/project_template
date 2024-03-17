def text_to_console(t):
    """
    Function for writing to console.

    Args:
        t (str): text to be written to console.
    """
    print("Printing to console: ", t)


def text_to_file(file_path, t):
    """
    Function for writing to file.

    Args:
        file_path (str): path to file where we will write text.
        t (str): text to be written to file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(t)
        print("Text was added to ", file_path)
    except Exception as e:
        print("Error ", str(e))
