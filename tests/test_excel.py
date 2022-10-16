from email import header
import sys
import os
import unittest
from my_dost.excel import *

header_value=1
def get_demo_df(header):
    file_path="tests/demo.xlsx"
    sheetname="Sheet1"
    df=excel_to_dataframe(input_filepath=file_path, input_sheetname=sheetname, header=header)
    return df

class test(unittest.TestCase):
    def test_write_excel_file(self):
        ## Case 1 - Complete inputs
        file_path="tests/test.xlsx"
        sheetname="Test_sheet"
        folder=file_path.split("/")[0]
        file_name=file_path.split("/")[1]
        excel_create_file(output_folder=folder, output_filename=file_name, output_sheetname=sheetname)
        assert os.path.exists(file_path)==True
        os.remove(file_path)

        ## Case 2 - Missing Sheetname
        file_path="tests/test.xlsx"
        folder=file_path.split("/")[0]
        file_name=file_path.split("/")[1]
        excel_create_file(output_folder=folder, output_filename=file_name)
        assert os.path.exists(file_path)==True
        os.remove(file_path)

        ## Case 3 - No xlsx at the end of the file name
        file_path="tests/test"
        sheetname="Test_sheet"
        folder=file_path.split("/")[0]
        file_name=file_path.split("/")[1]
        excel_create_file(output_folder=folder, output_filename=file_name, output_sheetname=sheetname)
        assert os.path.exists(file_path+".xlsx")==True
        os.remove(file_path+".xlsx")
    
    def test_excel_to_dataframe(self):
        df=get_demo_df(header_value)
    
    def test_excel_get_row_column_count(self):
        df=get_demo_df(header_value)
        count=excel_get_row_column_count(df)
        self.assertEqual(count, df.shape)
    
    def test_excel_set_single_cell(self):
        df=get_demo_df(header_value)
        text_to_replace="abc"
        column_name="Column 2"
        cell_number=3
        df=excel_set_single_cell(df, column_name, cell_number, text_to_replace)
        self.assertEqual(text_to_replace,df[column_name][cell_number-1])
    
    def test_excel_get_single_cell(self):
        df=get_demo_df(header_value)
        column_name="Column 2"
        cell_number=3
        self.assertEqual(df[column_name][cell_number-header_value-1], excel_get_single_cell(df, column_name, cell_number,header=header_value))

    def test_get_all_headers(self):
        df=get_demo_df(header_value)
        self.assertEqual(excel_get_all_header_columns(df),list(df.columns))

    def test_set_value_in_df(self):
        df=get_demo_df(header_value)
        row_number=1
        column_number=2
        value="abc"
        set_value_in_df(df, row_number, column_number, value)
        self.assertEqual(df.iloc[row_number-1,column_number-1], value)
if __name__ == '__main__':
    unittest.main()