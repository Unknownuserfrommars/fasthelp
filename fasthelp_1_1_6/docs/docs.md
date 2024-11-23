# Fasthelp Docs v1.1.3

## Custom Errors

### WillNotBeImplementedError

This shows a function or a class will NEVER be implemented. A little bit different to the `NotImplementeError`

### NoAPIEndpointError

Some classes / functions require calling the API, but the API Endpoint may not cover all the functions

## GetVersionInfo

### GetVersionInfo.__init()__

Initizalizes the GetVersionInfo class.

### GetVersionInfo.print()

Prints the version info

### GetVersionInfo.ret()

Returns the version info

### GetVersionInfo.pprint()

Calls the builtin `pprint` library and pretty prints the version info (Not quite sure the difference between the `print()` and the `pprint()`)

### Example code

```python
from fasthelp import *

gvi = GetVersioonInfo()

ret = gvi.ret()
gvi.pprint()
```

## DataHelper.new

### DataHelper.new.__init()__

Initizalizes the DataHelper.new object

### DataHelper.new.get_dataset()

From the DataHelper.new() object, this returns the dataset

### Example Code

```python
from fasthelp import *

datahelper_new = DataHelper.new('list()', 'my_list')
print(datahelper_new.get_dataset()) # Returns: []
```

## DataHelper.totype

### DataHelper.totype.Dataframe()

Turns the dataset into a pandas Dataframe / series.

### DataHelper.totype.list()

Turns the dataset into a list

### DataHelper.totype.dict()

Turns the dataset into a dict.

### DataHelper.totype.set()

Turns the dataset into a set.

### DataHelper.totype.npArray()

Turns the dataset into an NumPy array.

### Example Code:

```python
from fasthelp import *

my_list = [1,2,3,4,5]
array = DataHelper.totype.npArray(my_list)
```

## DataHelper.AdvancedList

### DataHelper.AdvancedList.apply()

Same as list.map()

### DataHelper.AdvancedList.select()

Same as list.filter()

### Example code

```python
from fastehlp import *

my_list = [1,2,3,101,102]
addone = lambda x: x+1
advlist = DataHelper.AdvancedList.apply(my_list)
print(advlist)
advlist = DataHelper.AdvancedList.select(addone, advlist)
```

## FileHelper.Open

### FileHelper.Open.__init(__)

Dummy function. This class haven't yet changed to full staticmethod (NOTE me that on 1.1.4), so it needs an __init(__) function to work.

### FileHelper.Open.Opentxt()

#### Needs init

Opens a text file (.txt suffix)

### FileHelper.Open.txt()

#### Needs init

Alias for FileHelper.Open.Opentxt()

### FileHelper.Open.Opencsv()

Opens a csv into a pandas DataFrame

### FileHelper.Open.Openexcel()

Opens an excel into a pandas DataFrame

### Example code

```python
from fasthelp import *

opentext = FileHelper.Open()
opentext.Opentxt('My.txt')

a = FileHelper.Open.Opencsv("My.csv")
b = FileHelper.Open.Openexcel("My.xlsx", 1)
```

## FileHelper.Create

### FileHelper.Create.Createtxt()

Creates a new .txt file

### FileHelper.Create.CreateDocument()

Creates a Word document (.doc/.docx)

### FileHelper.Create.CreatePresentation()

Creates a Powerpoint presentation (.ppt/.pptx)

### Example code

```python
from fasthelp import *

FileHelper.Createtxt('my_txt', 'D:\\Path\\to\\custon\\folder\\')
FileHelper.CreateDocument('Worddoc', "D:\\My\\Documents\\Folder\\")
FileHelper.CreatePresentation('Powerpnt', "D:\\A\\folder\\with\\presentations\\")
```

## StringHelper

### StringHelper.__init(__)

Initializes the original string

### StringHelper.Upper()

Uses string.upper(). The string is entered in the __init()__ function.

### StringHelper.Lower()

Uses string.lower()

### StringHelper.capitalize_letters()

Capitalizes some letters in the original string.

### StringHelper.lower_letters()

Lowercases some letters in the original string.

### StringHelper.lowercase_letters()

Returns ascii lowercase letters.

### StringHelper.uppercase_letters()

Returns all ascii uppercase letters.

### StringHelper.dedent()

Dedents the original string in the ______init(__).____

### Example Code

```python
import fasthelp as fh
string = fh.StringHelper("Hello")
u = string.Upper()
l = string.Lower()
HeLLo = string.capitalize_letters('L')
print(HeLLo)
```

## Missing some not useful functions. May replace them back in later versions.

## FolderHelper

### FolderHelper.__init()__

Initalizes the folder

### FolderHelper.listdir()

Lists the directory of the folder

### FolderHelper.makedir()

Creates a new, empty directory at the folder defined at __init(__)

### FolderHelper.makefile()

Creates a new file at the directory defined at __init(__)

### Example Code

```python
import fasthelp as fh
dir = fh.FolderHelper('C:\\Users\\pc\\Desktop\\some\\random\\folder\\')
print(dir.listdir())
dir.makedir('hello_world')
print(dirt.listdir())
dir.makefile(filename='helloworld')
```

## Some more classes missing

## OSHelper

### OSHelper.get_os_version()

Retreives the OS version

### OSHelper.get_system_architechure()

Gets the system architechure

### OSHelper.get_cpu_info()

Gets computer's CPU Info

### OSHelper.get_memory_usage()

Gets computer's RAM

### OSHelper.get_disk_space()

Gets computer's disk space

### OSHelper.get_network_info()

Retrieves the current network info

### OSHelper.get_system_uptime()

Returns the current system uptime

### OSHelper.get_running_processes()

Returns the number of current running processes

### OSHelper.get_computer_info()

Returns the CPU, GPU, and RAM info of the computer

### OSHelper.bundle()

Bundles all functions together

### Example Code

```python
import fasthelp as fh
print(fh.OSHelper.bundle())
```
