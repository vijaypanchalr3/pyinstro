import os
import inspect

def getpath():
        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame).pop()
        current_filename = caller_frame.filename
        return os.path.abspath(os.path.dirname(current_filename))