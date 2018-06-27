import cx_Freeze
from cx_Freeze import Executable
executables = [cx_Freeze.Executable("car crash.py")]

cx_Freeze.setup(
    name="Race game",
     options={"build_exe": {"packages":["pygame"],
                           "include_files":["car race.png","crashedcar.png","logo.png"]}},
    executables = executables
    
    )
