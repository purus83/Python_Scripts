import os
import subprocess


directory="c:\\tmp"
directory_contents_list=os.listdir(directory)

#size of directories


for dir_file in directory_contents_list:
  dir_file_size_command=subprocess.Popen(['dir', '/s', directory + "\\" + dir_file , '|', 'tail', '-2', '|', 'head' , '-1'],stdout=subprocess.PIPE, shell=True)
	dir_file_size_command_output=dir_file_size_command.communicate()[0]
	dir_file_size=dir_file_size_command_output.split()[2].replace(',','')
	dir_file_size_unit=dir_file_size_command_output.split()[3]
	print  dir_file, " - ", dir_file_size, " ", dir_file_size_unit
