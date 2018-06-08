import functions as func


def main():
    print("Welcome to 'The Concatenator'!")
    path = func.get_input()
    df = func.conc_files(func.file_list(path))
    writer = func.xlsx_writer()
    func.exp_xlsx(writer, df)
    func.another_file()


if __name__ == '__main__':
    main()
