import os
import sys
import pandas as pd
import main


def get_input():
    q = input("Are the files in the same folder? y/n")
    if q.lower() == 'y':
        # figure out the folder
        d = os.path.abspath(input("What's the directory?"))
        return os.path.abspath(d)
    elif q.lower() == 'n':

        """get first file, input second file, then ask if there are more long code, so fuck it for now"""

    else:
        print("pick 'y' or 'n' you dumb fuck!")


def file_list(directory):
    files = os.listdir(directory)
    ld = [os.path.join(directory, file) for file in files if file[-4:] == "xlsx"]
    return ld


def conc_files(filenames):
    df_from_each_file = list(map(pd.read_excel, filenames))
    concatenated_df = pd.concat(df_from_each_file)
    return concatenated_df


def xlsx_writer():
    writer = input("What file do you want to create?") + '.xlsx'
    return writer


def exp_xlsx(excel_path, df):
    writer = pd.ExcelWriter(excel_path)
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()


def another_file():
    inp = ''
    while inp == '':
        inp = input("Would you like to concatenate another file? y/n")
        if inp.lower() == 'y':
            main.main()
        elif inp.lower() == 'n':
            print("Thanks for using 'The Concatenator'! Goodbye!")
            sys.exit()
        else:
            print("Please choose either 'y' or 'n', you fucking ass-hat")
            continue
