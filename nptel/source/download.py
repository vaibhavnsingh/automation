import wget
import csv
import argparse
import os
from pathlib import Path
import sys

def file_exists():
    pass

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fileName', help="Name of the HTML File.e.g. a.html", required=True)
    parser.add_argument("-s","--skipCount",help = "No of files to skip. e.g. any postive integer value.", default=0)
    parser.add_argument("-t","--fileType",help="Type of file to download. eg ['pdf','mp4','flv','3gp','mp3']", default=["pdf","mp4"])
    parser.add_argument("-l","--log",help="CSV file name which will have the log. e.g. 'a.csv'", default="status.csv")
    args = parser.parse_args()
    return args

def return_url(line):
    print(line)
    try:
        url = line.split("href=")
        url_1= (url[1].replace('"',"")).replace('amp;',"")
        return url_1
    except Exception as e:
        print(e)
        return ""

def download_File(word):
    url = return_url(word)
    #output = download_File(url)  

    try:
        output  = wget.download(url)
        if "HTTP Error 404: Not Found" in output:
            raise Exception(output)
        else:
            writer.writerow([url,output,"PASS"])
    except Exception as e:
        print("error is : {}".format(e))
        writer.writerow([url, output,"FAIL"])

   

if __name__ == "__main__":
    try:
        get_args = get_arguments()
        html_file = Path(get_args.fileName)
        skip_count = int(get_args.skipCount)
        file_type = get_args.fileType
        if html_file.is_file():
            print("{} file found. Fetching the details to be downloded.".format(html_file))
            fread = open(html_file,"r")
        else:
            print("{} file not found. Exiting the program.".format(html_file))
            sys.exit(0)
        retrive_filetype = file_type.split(",")
        print("File type selected for download : {}".format(retrive_filetype))
        csv_filename = get_args.log
        csv_file = Path(get_args.fileName)

        fwrite = open(csv_file,"a")
        writer = csv.writer(fwrite)
        if csv_file.is_file():
            print("output will be written to : {}".format(csv_file))
        else:
            print("File not found")
            writer.writerow(["FILE NAME","URL", "DOWNLOAD STATUS"])      

        print("Summary : Source file name : {0}, Skip counter : {1}, File types to be downloded : {2}, Output file name : {3}".format(html_file, skip_count,file_type,csv_file))
    except Exception as e:
        print("Error is : {}".format(e))
    
    #sys.exit(0)

    try:
        #url=""
        count = 0
        for line in fread:
            words = line.split(" ")
            for word in words:
                if ("pdf" in retrive_filetype) and ("href" in word) and ("pdf" in word):
                    if skip_count > count :
                        count = count + 1
                        continue
                    download_File(word)
                elif ("mp4" in retrive_filetype) and ("href" in word) and (".mp4" in word):
                    if skip_count > count :
                        count = count + 1
                        continue
                    download_File(word)
                elif ("flv" in retrive_filetype) and ("href" in word) and (".flv" in word):
                    if skip_count > count :
                        count = count + 1
                        continue
                    download_File(word)
                elif ("3gp" in retrive_filetype) and ("href" in word) and (".3gp" in word):
                    if skip_count > count :
                        count = count + 1
                        continue
                    download_File(word)
                elif ("mp3" in retrive_filetype) and ("href" in word) and ("mp3" in word):
                    if skip_count > count :
                        count = count + 1
                        continue
                    download_File(word)
    except Exception as e:
        print("Error is {}".format(e))