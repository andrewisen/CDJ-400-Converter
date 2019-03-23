#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written by: Andre MG Wisen
# https://andrewisen.se/
import os

def main():
	# === SETTINGS ===
	delimiter = "."
	filenameSuffix = "mp3"
	currentDirectory = os.getcwd()

	try:
		for root, directories, files in os.walk(currentDirectory):
				for file in files:
					try:
						filename, suffix = file.split(delimiter)
						continue
					except:
						pass
					oldFile = os.path.join(root, file)
					newFile = oldFile + delimiter + filenameSuffix
					print(oldFile,newFile)
					os.rename(oldFile, newFile)
	except Exception as e:
		print(e)
	return
if __name__== "__main__":
	main()