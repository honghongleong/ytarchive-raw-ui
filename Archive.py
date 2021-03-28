from configparser import ConfigParser
import os
import subprocess

#Get the configparser object
config_object = ConfigParser()

def check_config():
    #Check if config file exist
    if os.path.exists("./config.ini"):
        #Check if user wants to update config file
        check = input("Does config file needs to be updated?:")
        if check.lower() in ('y', 'yes'):
            config_object.read("config.ini")
            #Get the USERINFO section
            updateinfo = config_object["Config"]
            #Updating of Config file
            threads = input("Input amount of threads: ")
            output = input("Input output location: ")
            tempdir = input("Input temp file directory: ")
            updateinfo["threads"] = threads
            updateinfo["output"] = output
            updateinfo["tempdir"] = tempdir
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
        elif check.lower() in ('n', 'no'):
            pass
        else:
            print("Invalid Input")
            check_config()
    if not os.path.exists("./config.ini"):
        threads = int(input("Input amount of threads: "))
        output = str(input("Input output location: "))
        tempdir = str(input("Input Tempoary Directory location: "))
        #Creating of config file
        config_object["Config"] = {
            "threads": threads,
            "output": output,
            "tempdir": tempdir
        }
        #Write the above sections to config.ini file
        with open('config.ini', 'w') as conf:
            config_object.write(conf)


try:
    check_config()
    file = input("Do you wish to use JSON file instead of URL?: ")
    if file.lower() in ('y','yes'):
        currentDirectory = os.getcwd()
        json = currentDirectory + "\\" + str(input("Please input the JSON location: "))
        #json = currentDirectory + "\\" +"test.json"
        
    elif file.lower() in ('n','no'):
        video = str(input("Please input video URL: "))
        audio = str(input("Please input audio URL: "))
    else:
        print("Invalid Input")
    config_object = ConfigParser()
    config_object.read("config.ini")
    configuration = config_object["Config"]
    #"-o",configuration["output"] 
    #"-td",configuration["tempdir"]  
    subprocess.call(["python",".\index.py", "-i", json ,"-t",configuration["threads"]])
	

except:
    exit()
