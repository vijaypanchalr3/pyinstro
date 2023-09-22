from pyinstro.utils import getpath



import csv
import os



class Get_File:
    """
    INFO: just to write file, must be CSV 
    """
    def __init__(self,file) -> None:
        _project_dir_path_abs = getpath.getpath()

        if os.path.exists(os.path.join(_project_dir_path_abs,"data")):
            _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")
        else:
            os.mkdir(os.path.join(_project_dir_path_abs,"data"))
            _data_dir_path_abs = os.path.join(_project_dir_path_abs,"data")
        
        if file=='default':
            file = "auto0.csv"
            count = 0
            while os.path.exists(os.path.join(_data_dir_path_abs,f"auto{count}.csv")):
                count+=1
                file = f"auto{count}.csv"

        file = os.path.join(_data_dir_path_abs,file)
        
        # i did not used re module down here
        if not ((file[len(file)-1]=='v')and(file[len(file)-2]=='s')and(file[len(file)-3]=='c')and(file[len(file)-4]=='.')):
            file = file+".csv"
        else:
            pass
        
        self.filepath = file
        self.firsttime = True

    def writerow(self, data)-> None:
        """
        open file one time ad write it
        """
        if self.firsttime:
            self.file = open(self.filepath,'w',newline='')
            self.writer = csv.writer(self.file)
            self.writer.writerow(data)
            self.firsttime = False
            print(self.filepath)
        else:
            self.writer.writerow(data)


    def longwriterow(self,data)->None:
        """
        for long data, i think it is suitable to write file each time open and close
        """
        with open(self.filepath,'a',newline="") as datafile:
            self.writer = csv.writer(datafile)
            self.writer.writerow(data)

            
    


    