import os
import os.path
import time
from datetime import datetime
from glob import glob

class PictureMover:

	def __init__(self, workdirectory, destinationdirectory, extensions):
	    self.workdirectory = workdirectory
	    self.destinationdirectory = destinationdirectory
	    self.extensions = extensions

	def do_work(self):
		for file_to_move in self.get_files_to_move():
			subdirectoryname = self.get_subdirectoryname(file_to_move)
			self.create_directory_if_not_exits(subdirectoryname)
			os.rename(file_to_move, self.get_filename_after_move(subdirectoryname, file_to_move))

	def get_files_to_move(self):
		files_to_move = []
		workdirectory_and_subdirectories = self.get_workdirectory_and_subdirectories()

		for current_directory in workdirectory_and_subdirectories:
			for extension in self.extensions:
				extension_wildcard_path = current_directory + '/*.' + extension
				files_to_move.extend(glob(extension_wildcard_path))

		return files_to_move

	def get_workdirectory_and_subdirectories(self):
		return [x[0] for x in os.walk(self.workdirectory)]

	def get_subdirectoryname(self, filename):
		return os.path.join(self.destinationdirectory + self.get_year_and_month(filename))

	def get_filename_after_move(self, directoryname, filename):
		return os.path.join(directoryname, os.path.basename(filename))

	def get_year_and_month(self, filename):
		return datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y - %m')

	def create_directory_if_not_exits(self, directoryname):
		if not os.path.isdir(directoryname):
			os.makedirs(directoryname)
