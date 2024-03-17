import app.io.input as aii
import app.io.output as aio

def main():
    a = aii.text_fr_console()
    aio.text_to_console(a)
    b = aii.text_fr_file("datafile.txt")
    aio.text_to_file("datafile_res.txt", b)
    c = aii.text_fr_file_pandas("datafile.txt")
    aio.text_to_file("datafile_res_from_pandas.txt", c)


if __name__ == "__main__" :
    main()
