# -*- coding: utf-8 -*-


class Storage:
	def store(self, filename, content):
		raise NotImplementedError
	
	def read(self, filename):
		raise NotImplementedError
