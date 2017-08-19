from urllib.request import urlopen
import json
import sys
import subprocess, shlex
import os
workdir=sys.argv[1]
gitlabhost=sys.argv[2]
token=sys.argv[3]
print('workdir:%s host:%s token=%s'%(workdir,gitlabhost,token))

if not os.path.exists(workdir) or not os.path.isdir(workdir):
    print('dir %s not exists'%(workdir))
    exit()


print('workdir:%s'%(os.getcwd()))
page=1
allProjectsDict=[]
while page==1 or len(allProjectsDict)==100:
    print('http://%s/api/v3/projects?private_token=%s&per_page=100&page=%d'%(gitlabhost,token,page))
    allProjects= urlopen('http://%s/api/v3/projects?private_token=%s&per_page=100&page=%d'%(gitlabhost,token,page))
    page=page+1
    allProjectsDict = json.loads(allProjects.read().decode())
    for thisProject in allProjectsDict: 
        try:
            os.chdir(workdir)
            thisProjectURL  = thisProject['ssh_url_to_repo']
            tpath=workdir+"/"+thisProject['namespace']['path']
            if not os.path.exists(tpath):
                print('mkdir %s' % (thisProject['namespace']['path']))
                command     = shlex.split('mkdir %s' % (thisProject['namespace']['path']))
                resultCode  = subprocess.Popen(command)
            if not os.path.exists(workdir+"/"+thisProject['path_with_namespace']):
                os.chdir(tpath)
                print('git clone %s' % thisProjectURL)
                command     = shlex.split('git clone %s' % thisProjectURL)
                resultCode  = subprocess.Popen(command)
            else:
                print('git pull %s' % thisProjectURL)
                os.chdir(workdir+"/"+thisProject['path_with_namespace'])
                command     = shlex.split('git pull')
                resultCode  = subprocess.Popen(command)
        except Exception as e:
            print("Error on %s: %s" % (thisProjectURL, e.strerror))