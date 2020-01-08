#!/usr/bin/python3

import time, sys, os, datetime, argparse, platform
from os import listdir, chdir, path, mkdir, replace, stat
from os.path import isfile, join, getctime, exists

def creation_date(path):
    if platform.system() == 'Windows':
        return getctime(path_to_file)
    else:
        st = stat(path)
        try:
            return st.st_birthtime
        except AttributeError:
            return st.st_mtime

dateformat = '%d/%m/%Y'

def convert_date(str):
    return datetime.datetime.strptime(str, dateformat)

parser = argparse.ArgumentParser(
    description='''Script for add files within a date range in a directory ''')
parser.add_argument("dir", help='input directory')
parser.add_argument("-n", "--name", default='Unknown', help='output directory')
parser.add_argument("-s", "--startdate", help='set start day')
parser.add_argument("-e", "--enddate", help='set end day')
parser.add_argument("-d", "--day", help='add files with day specified')
parser.add_argument("-y", "--year", help='add files with year specified')
args = parser.parse_args()


if (args.day):
    args.startday = args.day
    args.enddate = args.day

if (args.year):
    args.startday = '01/01/' + args.year
    args.enddate = '31/12/' + args.year

name = args.name

files = [f for f in listdir(args.dir) if isfile(join(args.dir, f))]
chdir(args.dir)

if not(exists(name)):
    mkdir(name)
datedir = []
for f in files:
    t = datetime.datetime.strptime(time.ctime(creation_date(f)), "%a %b %d %H:%M:%S %Y")
    if ((not args.startday) or t >= convert_date(args.startday)) and ((not args.enddate) or t <= (convert_date(args.enddate) + datetime.timedelta(days=1))):
        print(name + '/' + f)
        replace(f, name + '/' + f)
