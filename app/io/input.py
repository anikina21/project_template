import pandas


def text_fr_console():
    return input("Enter text: ")


def text_fr_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("The file wasn't found")
        return None


def text_fr_file_pandas(file_path):
    try:
        data = pandas.read_csv(file_path, sep='\n', header=None)
        return ' '.join(data[0].tolist())
    except FileNotFoundError:
        print("The file wasn't found")
