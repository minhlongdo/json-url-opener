# -*- coding: utf-8 -*-
from storage.storage import Storage

import json
import os


class JsonStorage(Storage):
	def __init__(self, storage_url=None):
		if storage_url is None:
			self.storage_url = ""
		else:
			self.storage_url = storage_url
	
	def read(self, filename):
		if filename is None:
			raise ValueError("Filename must be not None")
		
		if len(self.storage_url) == 0:
			actual_filename = filename
		else:
			actual_filename = self.storage_url + "/" + filename
		
		print("Actual filename " + actual_filename)
		
		# Check if file exists
		if not os.path.exists(actual_filename):
			raise FileNotFoundError("file " + actual_filename + " not found")
		
		try:
			json_data = open(actual_filename).read()
			if json_data is not None:
				data = json.loads(json_data)
				return data
			
			else:
				return None
				
		except IOError:
			raise IOError("Something happened during reading the json file %s", actual_filename)
		
		except Exception:
			raise Exception("Something unexpected happened")

	def store(self, filename, content):
		if filename is None or content is None or len(filename) == 0 or len(content) == 0:
			raise ValueError("Either invalid filename or content")
		
		if len(self.storage_url) == 0:
			actual_filename = filename
		else:
			actual_filename = self.storage_url + "/" + filename
		
		with open(actual_filename, "w", encoding="utf-8") as f:
			json.dump(content, f, ensure_ascii=False)
