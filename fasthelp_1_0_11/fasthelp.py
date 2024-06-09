import pandas as pd
import numpy as np
import pprint

class _GetVersionInfo:
    def __init__(self):
        self._versionInfoMessage = "You are using FastHelp version 1.0.11, developed by JDT."
    def print(self):
        print(self._versionInfoMessage)
    def ret(self):
        return self._versionInfoMessage
    def pprint(self):
        pprint.pprint(self._versionInfoMessage)

class DataHelper:
    class new:
        def __init__(self, data_type, save_name):
            """
            You are using `DataHelper.new()`, developed by JDT, version 0.7.19.
            Creates a empty dataset (e.g.: list, dict, pd.DataFrame, etc.)

            Parameters:
            data_type (keyword): Enter a dataset type (e.g.: `list`, `dict`, `pd.DataFrame`, etc.) (NOTE: When you enter the data_type, DO NOT add brackets (for example, `list` not `list()`))
            save_name (str): The name of the dataset

            Returns:
            data_type: A dataset (type based on the input parameter 'data_type')
            """
            try:
                exec(f'{save_name} = {data_type}()')
            except Exception as e:
                raise SyntaxError(f"Invalid Syntax, an error happened. Error message: {e}")
    class totype:
        def DataFrame(self, dataset):
            """
            You are using `DataHelper.totype.DataFrame()`, developed by JDT, version 0.1.0.
            Change a dataset to a pd.DataFrame (Or pd.Series)
            
            Parameter:
            dataset (data set): The original dataset you want to change the type.

            Returns:
            pd.DataFrame or pd.Series
            """
            if not isinstance(dataset, (pd.DataFrame, pd.Series)):
                return pd.DataFrame(dataset)
            else:
                raise TypeError(f'The dataset you\'ve entered is a {type(dataset)} type. Which is not supported.')
            
        def list(self, dataset):
            """
            You are using `DataHelper.totype.list()`, developed by JDT, version 0.1.3.
            Change a dataset to a Python list.
            
            Parameter:
            dataset (data set): The original dataset you want to change the type.

            Returns:
            list: The list
            """
            if not isinstance(dataset, list):
                try:
                    return list(dataset)
                except Exception as e:
                    raise SyntaxError(f'An error occured while turning the dataset {dataset} to a list: {e}')
            else:
                raise TypeError(f'The dataset that you\'ve entered is a {type(dataset)} type. Which is not okay.')
            
        def dict(self, dataset):
            """
            You are using `DataHelper.totype.dict()`, developed by JDT, version 0.1.3.
            Change a dataset to a Python dictionary.
            
            Parameter:
            dataset (data set): The original dataset you want to change the type.

            Returns:
            dict: The dictionary
            """
            if not isinstance(dataset, dict):
                try:
                    return dict(dataset)
                except Exception as e:
                    raise SyntaxError(f'An error occured while turning the dataset {dataset} to a dictionary: {e}')
            else:
                raise TypeError(f'The dataset that you\'ve entered is a {type(dataset)} type. Which is not supported.')
        
        def Array(self, dataset):
            """
            You are using `DataHelper.totype.Array()`, developed by JDT, version 0.3.2.
            Change a dataset to a numpy Array.
            
            Parameter:
            dataset (data set): The original dataset you want to change the type.

            Returns:
            np.array: The numpy Array
            """
            if not isinstance(dataset, np.ndarray):
                try:
                    return np.array(dataset)
                except Exception as e:
                    raise SyntaxError(f'An error occured while turning the dataset {dataset} to a np.Array: {e}')
            else:
                raise TypeError(f'The dataset that you\'ve entered is a {type(dataset)} type. Which is not supported.')
        
    # Add more if needed
            
class future:
    class About:
        def __init__(self):
            self._about_future = "the `future` module contains many future implementations. Developed by JDT, version 0.3.0."
        def print(self):
            print(self._about_future)
        def ret(self):
            return self._about_future
        def pprint(self):
            pprint.pprint(self._about_future)

    class Full_Read_Csv:
        def __init__(self, **kwargs):
            self.FirstAppearVersion = "1.0.9"
            self.FirstImplementVersion = "1.3.0"  # Hopefully...
            return pd.read_csv(**kwargs)
        
    class Full_Read_Excel:
        def __init__(self, **kwargs):
            self.FirstAppearVersion = "1.0.10"
            self.FirstImplementVersion = "1.3.0"
            return pd.read_excel(**kwargs)
        
    class No_More_JDT:
        def __init__(self):
            """
            Congrats, you've found an easter egg!
            """
            self.FirstAppearVersion = "1.0.0"
            self.FirstImplementVersion = "12345678900.0.0"
            self.Note = "JDT FOREVER!!!"

class FileHelper:
    class Open:
        def __init__(self):
            pass
        
        def Opentxt(self, file, name=None):
            """
            You are using `FileHelper.Open.Opentxt()`, developed by JDT, version 0.2.14.
            Currently, it only supports opening a file with read-only mode. More modes will be added in the future.

            Parameters:
            file: The .txt file you want to open.
            name (Optional): return the file with a name.

            Returns:
            An opened file
            """
            if name:
                with open(file) as name:
                    return name
            else:
                return open(file)
        
        def txt(self, file, name=None):
            """Wrapper function for `Opentxt()`, version 0.1.0."""
            if name:
                return Opentxt(file, name)  # noqa: F821
            else:
                return Opentxt(file)  # noqa: F821
            
        def Opencsv(self, file, sep=None, delimiter=None, header=None, index_col=None):
            """
            You are using `FileHelper.Open.Opencsv()`, developed by JDT, version 0.4.2.
            Currently, it only supports few keyword arguments. More arguments will be added in the future.

            Parameters:
            file: The .csv file you want to open
            (Optional arguments:)
            sep: 
            delimiter:
            header:
            index_col:

            Returns:
            pd.DataFrame: Can be used with `DataHelper.totype`

            Example:
            `DataHelper.totype.dict(FileHelper.Open.Opencsv("C:/Users/usr/Desktop/Folder/testcsv/csv1.csv"))`
            """
            return pd.read_csv(file, sep, delimiter, header, index_col=index_col)
        
        def Openexcel(self, file, sheet_name, index_col=None):
            """
            You are using `FileHelper.Open.Openexcel()`, developed by JDT, version 0.5.11.

            Parameters:
            file: file path to the .xls/.xlsx file
            sheet_name: the name of the specific sheet(s)
            index_col (Optional): Column indexes

            Returns:
            pd.DataFrame
            """
            return pd.read_excel(file, sheet_name, index_col=index_col)
        
        # Add more if needed

class StringHelper:
    def Upper(string: str) -> str:
        """
        You are using `StringHelper.Upper()`, developed by JDT, version 0.3.1.

        Parameter:
        string (`str`): the original string

        Returns:
        str
        """
        return string.upper()
    
    def Lower(string: str) -> str:
        """
        You are using `StringHelper.Lower()`, developed by JDT, version 0.3.1.

        Parameter:
        string (`str`): the original string

        Returns:
        `str`
        """
        return string.lower()
    
    def capitalize_letters(text: str, letters) -> str:
        """
        You are using `String.capitalize_letters()`, developed by JDT and ElectroBL, version 0.2.11.

        Parameters:
        text (`str`): the original text
        letters (`str` or list of `str`): the letters you want to capitalize in the original string

        Returns:
        str
        """
        letters_set = set(letters)
        capitalized_text = ''.join([char.upper() if char in letters_set else char for char in text])
        return capitalized_text
    
    def lower_letters(text: str, letters) -> str:
        """
        You are using `String.lower_letters()`, developed by JDT, version 0.1.3.

        Parameters:
        text (`str`): the original text
        letters (`str` or list of `str`): the letters you want to lower in the original string

        Returns:
        str
        """
        letters_set = set(letters)
        lowered_text = ''.join([char.lower() if char in letters_set else char for char in text])
        return lowered_text