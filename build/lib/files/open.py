import pandas as pd

class open:
    @staticmethod
    def opentxt(file: str, write_mode: bool = False):
        mode = 'w' if write_mode else 'r'
        try:
            return open(file, mode)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{file}' does not exist.")

    def csv(filepath: str, **kwargs) -> pd.DataFrame:
        """
        Opens a CSV file as a pandas DataFrame.

        Parameters:
        filepath (str): Path to the .csv file.
        **kwargs: Additional arguments for pandas.read_csv().

        Returns:
        pd.DataFrame: DataFrame representation of the CSV file.
        """
        try:
            return pd.read_csv(filepath, **kwargs)
        except Exception as e:
            raise FileNotFoundError(f"An error occurred while opening the CSV file: {e}")

    def excel(filename: str, sheet_name=0, index_col=None) -> pd.DataFrame:
        """
        Opens an Excel file as a pandas DataFrame.

        Parameters:
        filename (str): Path to the Excel file (.xls or .xlsx).
        sheet_name (Optional): Sheet name or index. Default is the first sheet.
        index_col (Optional): Column index to use as row labels.

        Returns:
        pd.DataFrame: DataFrame representation of the Excel sheet.
        """
        try:
            return pd.read_excel(filename, sheet_name=sheet_name, index_col=index_col)
        except Exception as e:
            raise FileNotFoundError(f"An error occurred while opening the Excel file: {e}")
