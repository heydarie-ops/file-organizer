# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:25:07 2026

@author: Mohammad Mehdi

project : file organizer V102

"""

import os
import argparse
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("path_arg", help = "this program organazie the folder you ask")
parser.add_argument("--dry-run", help = "this feature just show you how this programe work",action="store_true")
args = parser.parse_args() # see what user wirte in command line and analyse that

path = args.path_arg

#path = r"D:\test"

directories ={"photo":[".jpg",".jpeg",".gif",".bmp",".svg",".webp",".tiff",".ico"],
              "Documents":[".pdf",".doc",".docx",".txt",".rtf",".odt"],
              "Excel":[".xls",".xlsx",".csv",".ods"],
              "PowerPoint":[".ppt",".pptx",".odp"],
              "Video":[".mp4",".mkv",".avi",".mov",".wmv",".flv",".webm"],
              "Audio":[".mp3",".aac",".ogg",".m4a",".wav",".flac"],
              "Archive":[".zip",".rar",".7z",".tar",".gz"],
              "code":[".py",".js",".css",".java",".sql",".json"],
              "application":[".exe",".bat",".sh",".msi",".appimage"]}


file_lst = os.listdir(path) #reading the files 
for file in file_lst:
    file_ext_tp = os.path.splitext(file) # trying to find file extention
    for key,values in directories.items():
        if file_ext_tp[1] in values:
            source = os.path.join(path,key)
            if not os.path.exists(source) and not(args.dry_run):
                os.mkdir(source) #creating the folders
                print(key)
            if args.dry_run:
                print(f"{file} ----> {key}")
            else:
                os.replace(os.path.join(path,file),os.path.join(source, file))
                with open("log.txt","a",encoding="utf-8") as log_file:
                    log_file.write(f"{datetime.datetime.now()} -- {file} from {path} --------->> {source}\n")
          





