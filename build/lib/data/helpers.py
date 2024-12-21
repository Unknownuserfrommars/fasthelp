import pandas as pd
import numpy as np


# Submodule for dataset creation
class create:
    def __init__(self, data_type, save_name: str):
        """
        Creates an empty dataset (any valid Python data structure or custom object).

        Parameters:
        data_type (`str`): Enter a dataset type (e.g.: `list()`, `dict()`, `pd.DataFrame()`, etc.)
                          (NOTE: Use brackets (e.g., `list()` not `list`)).
        save_name (`str`): The name of the dataset.

        Returns:
        data_type: A dataset (type based on the input parameter 'data_type').

        Example:
        ```python
        creator = create('list()', 'my_list')
        print(creator.get_dataset())  # Output: []
        ```
        """
        try:
            loc_con = {}
            exec(f'{save_name} = {data_type}', {}, loc_con)
            self.dataset = loc_con[save_name]
            setattr(self, save_name, self.dataset)
        except Exception as e:
            raise SyntaxError(f"Failed to create dataset. Error: {e}")
        
    def get_dataset(self):
        """
        Returns the created dataset.
        """
        return self.dataset

    def get_df(self):
        """
        Alias for .get_dataset()
        New in v1.2.0
        """
        return self.dataset

class manipulate:
    def __init__(self, dataset):
        """
        Manipulates a dataset (e.g., adds or removes elements).

        Parameters:
        dataset: The dataset to be manipulated.

        Returns:
        dataset: The manipulated dataset.

        Example:
        ```python
        my_list = [1, 2, 3]
        manipulator = manipulate(my_list)
        manipulator.add_element(4)
        print(manipulator.get_dataset())  # Output: [1, 2, 3, 4]
        ```
        """
        self.dataset = dataset

    def get_dataset(self):
        """
        Returns the created dataset.
        """
        return self.dataset

    def add_element(self, element):
        """
        Adds an element to the dataset.

        Parameters:
        element: The element to be added.

        Example:
        ```python
        manipulator.add_element(4)
        ```
        """
        if isinstance(list, self.dataset):
            self.dataset.append(element)
        else:
            raise TypeError("add_element currently only supports appending to lists. Implementation for more can be expected in 1.4.0. (If you want it to be done faster, talk in Github repo)")

    def remove_element(self, element):
        """
        Removes an element from the dataset.

        Parameters:
        element: The element to be removed.

        Example:
        ```python
        manipulator.remove_element(4)
        ```
        """
        if not isinstance(list, self.dataset):
            raise TypeError('remove_element currently only supports appending to lists. Implementation for more can be expected in 1.4.0. (If you want it to be done faster, talk in Github repo)')
        if element not in self.dataset:
            raise ValueError(f"The element {element} is not in the dataset.")

        # Rebuild the list excluding the element
        self.dataset = [item for item in self.dataset if item != element]
        return self.dataset

    def get_df(self):
        """
        Alias for.get_dataset()
        New in v1.2.0
        """
        return self.dataset

# Submodule for data type conversions
class convert:
    @staticmethod
    def to_dataframe(dataset) -> pd.DataFrame:
        """
        Converts a dataset to a pandas DataFrame (or Series).
        """
        if not isinstance(dataset, (pd.DataFrame, pd.Series)):
            return pd.DataFrame(dataset)
        else:
            raise TypeError(f"The dataset is already of type {type(dataset)}.")

    @staticmethod
    def to_list(dataset) -> list:
        """
        Converts a dataset to a Python list.
        """
        if not isinstance(dataset, list):
            try:
                return list(dataset)
            except Exception as e:
                raise SyntaxError(f"Failed to convert dataset to list: {e}")
        else:
            raise TypeError(f"The dataset is already of type {type(dataset)}.")

    @staticmethod
    def to_dict(dataset) -> dict:
        """
        Converts a dataset to a Python dictionary.
        """
        if not isinstance(dataset, dict):
            try:
                return dict(dataset)
            except Exception as e:
                raise SyntaxError(f"Failed to convert dataset to dict: {e}")
        else:
            raise TypeError(f"The dataset is already of type {type(dataset)}.")

    @staticmethod
    def to_set(dataset) -> set:
        """
        Converts a dataset to a Python set.
        """
        if not isinstance(dataset, set):
            try:
                return set(dataset)
            except Exception as e:
                raise SyntaxError(f"Failed to convert dataset to set: {e}")
        else:
            raise TypeError(f"The dataset is already of type {type(dataset)}.")

    @staticmethod
    def to_np_array(dataset) -> np.ndarray:
        """
        Converts a dataset to a numpy array.
        """
        if not isinstance(dataset, np.ndarray):
            try:
                return np.array(dataset)
            except Exception as e:
                raise SyntaxError(f"Failed to convert dataset to numpy array: {e}")
        else:
            raise TypeError(f"The dataset is already of type {type(dataset)}.")

    # More will be added later!
