import platform
import subprocess

def get_gpu_info() -> (list[str] | str):
    """
    Welcome to gpuinfo.py!
    This is a function targeted to retrieve the GPU info of the computer in MacOS, Windows and Linux.
    This is developed by and only by FastHelp Dev.
    This module is targeted as a patch to the `OSHelper.get_computer_info()` function in the main python file (fasthelp.py)
    """
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            result = subprocess.run(['system_profiler', 'SPDisplaysDataType'], stdout=subprocess.PIPE)
        elif os_name == "Windows":
            result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'description'], stdout=subprocess.PIPE)
            output = result.stdout.decode().strip().split('\n')[1:]
            return [line.strip() for line in output if line.strip()]
        elif os_name == "Linux":
            result = subprocess.run(['lspci', '-vnn'], stdout=subprocess.PIPE)
            return result.stdout.decode()
        else:
            return "Unsupported OS or missing GPU tools."
        return result.stdout.decode()
    except Exception as e:
        return f"Error retrieving GPU info: {str(e)}"