#!/usr/bin/python

# Imports
import os, re, subprocess, datetime

##### EDIT ME CONFIG ######
backuproot = "/mnt/user/Backups/"
configroot = "/mnt/cache/config/"

# Variables
now = datetime.datetime.now()
date = str(now.year)+str(now.month)+str(now.day)+"-"+str(now.hour)+str(now.minute)
backupdir = backuproot + date
docker_images =  re.findall("\/(\S+)", os.popen("docker inspect --format='{{.Name}}' $(sudo docker ps -q --no-trunc)").read())

# Make the backup directory
subprocess.call(["mkdir", "-p",  backupdir])

# Stop and docker images and tar the config files, then start the image again.
for image in docker_images:
    tarball = date + "." + image + ".tar.gz"
    subprocess.call(["docker", "stop", image])
    subprocess.call(["tar", "-pczf", backupdir + "/" + tarball, configroot + image.lower()])
    subprocess.call(["docker", "start", image])




