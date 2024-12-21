# Expose subpackages and main utilities
from .data import create as dcreate, convert, manipulate
from .files import open, create as fcreate
from .strings import strings
from .system import OS, get_gpu_info
from .opers import LogicalOps
from .imports import DynamicImporter, PipHelper
from .plots import PXUtils
from .utils import VersionInfo, DeprecationHelper

# Define the public API
__all__ = [
    "dcreate", "convert", "manipulate",
    "open", "fcreate",
    "strings",
    "OS", "get_gpu_info",
    "LogicalOps",
    "DynamicImporter", "PipHelper",
    "PXUtils",
    "VersionInfo", "DeprecationHelper"
]

# Package Metadata
__version__ = VersionInfo.get_version()
__author__ = VersionInfo.get_author()
__license__ = VersionInfo.get_license()

# Optional Initialization Function
def initialize():
    """
    Initialize the FastHelp package (e.g., for dependency checks or startup messages).
    """
    print(VersionInfo.full_info())
    print("FastHelp is ready to assist you. 🚀")
