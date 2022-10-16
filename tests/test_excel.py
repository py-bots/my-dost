from email import header
from fcntl import F_SEAL_SEAL
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

    def test_get_value_in_df(self):
        df=get_demo_df(header_value)
        row_number=1
        column_number=2
        value=get_value_in_df(df, row_number, column_number)
        self.assertEqual(df.iloc[row_number-1,column_number-1], value)

    def test_df_drop_rows(self):
        df=get_demo_df(header_value)
        total_rows=df.shape[0]
        start_row=2
        end_row=3
        df=df_drop_rows(df, start_row,end_row)
        self.assertEqual(df.shape[0], total_rows-(end_row-start_row))   ## as we are deleting both starting and ending rows

    def test_df_extract_sub_df(self):
        df=get_demo_df(header_value)
        start_row=2
        end_row=5
        start_column=2
        end_column=4
        modified_df=df_extract_sub_df(df, start_row, end_row, start_column, end_column)
        df=df.iloc[start_row-1:end_row-1,start_column-1:end_column-1]
        self.assertEqual(df.equals(modified_df),True)
    
    def test_excel_clear_sheet(self):
        df=get_demo_df(header_value)
        df=excel_clear_sheet(df)
        self.assertEqual(df.empty,True)
        # self.assertEqual(df.columns.empty,False)
        
if __name__ == '__main__':
    unittest.main()