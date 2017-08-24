from urllib.request import urlopen
import json
import sys
import subprocess, shlex
import os
import ssl
workdir=sys.argv[1]
gitlabhost=sys.argv[2]
token=sys.argv[3]
protocol="http"
#print(sys.argv)
if len(sys.argv)>=5:
    protocol=sys.argv[4]
print('workdir:%s host:%s token=%s %s'%(workdir,gitlabhost,"token",protocol))

if not os.path.exists(workdir) or not os.path.isdir(workdir):
    print('dir %s not exists'%(workdir))
    exit()

ssl._create_default_https_context = ssl._create_unverified_context

print('workdir:%s'%(os.getcwd()))
page=1
allProjectsDict=[]
while page==1 or len(allProjectsDict)==100:
    print('%s://%s/api/v3/projects?private_token=%s&per_page=100&page=%d'%(protocol,gitlabhost,"token",page))
    allProjects= urlopen('%s://%s/api/v3/projects?private_token=%s&per_page=100&page=%d'%(protocol,gitlabhost,token,page))
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
                #os.chdir(tpath)
                print('git clone %s' % thisProjectURL)
                command     = shlex.split('git clone %s' % thisProjectURL)
                resultCode  = subprocess.Popen(command,cwd=tpath)
            else:
                print('git pull %s' % thisProjectURL)
                #os.chdir(workdir+"/"+thisProject['path_with_namespace'])
                command     = shlex.split('git pull')
                resultCode  = subprocess.Popen(command,cwd=workdir+"/"+thisProject['path_with_namespace'])
            resultCode.communicate()
        except Exception as e:
            print("Error on %s: %s" % (thisProjectURL, e.strerror))