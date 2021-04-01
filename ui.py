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
'''
#Code testing
def hi_json():
    # other code...
    hi_json.bye = 42  # Create function attribute.
    hi_json.test = input("please input a numbaer:")
'''

try:
    check_config()
    #Update Json input methods
    json = input("Please input Json file or video URL: ")
    extension=os.path.splitext(str(json))[1]
    if "https://" in json or "---sn" in json:
        video = json
        audio = input("Please input audio URL: ")
    elif os.path.isfile(json) and ".json" in extension:
        json = json
    elif ".json" in json:
        currentDirectory = os.getcwd()
        json = currentDirectory + "\\" + str(json)
    else:
        print("Invalid Input")
    
    config_object = ConfigParser()
    config_object.read("config.ini")
    configuration = config_object["Config"]
    #"-o",configuration["output"] 
    #"-td",configuration["tempdir"] 
    subprocess.call(["python", "./index.py", "-i", json ,"-t",configuration["threads"]])

except:
    exit()
