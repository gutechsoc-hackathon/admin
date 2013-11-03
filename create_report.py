import subprocess
import StringIO
import os, sys
sshaddress = "git@github.com:gutechsoc-hackathon/"
repos = set(("segfault", "geeksoc", "javatar", "Django", "sammo", "devnull", "EasternBlock", "TeamZero", "while1", "atlas", "Stefan",))

extensions = set(("cpp", "php", "h", "c", "hpp", "hpp", "java", "py", "yml", "js", "html", "xml", "sql", "css"))

def clone(address = sshaddress, repos = repos):
    for repo in repos:
        subprocess.call("cd .. && git clone " + sshaddress + repo, shell=True)

def pull(address = sshaddress, repos = repos):
    for repo in repos:
        print repo
        subprocess.call("cd ../" + repo + " && git fetch origin master && git reset --hard FETCH_HEAD", shell=True)

def countlines(project, extension):
    if os.path.exists("tmp"):
        os.remove("tmp")
    if os.path.exists("tmp2"):
        os.remove("tmp2")
    with open("tmp", "w") as filelist:
        process1 = subprocess.Popen("find " + project + "/* | grep ." + extension, stdout = filelist, shell=True)
        process1.wait()
    with open("tmp", "r") as filelist:
        with open("tmp2", "w") as inneroutput:
            for filename in filelist.readlines():
                if filename.split(".")[-1][:-1] == extension:
                    #print filename.split(".")
                    process = subprocess.Popen("wc -l " + filename, stdout = inneroutput, shell = True)
                    process.wait()
        with open("tmp2", "r") as inneroutput:
            suma = 0
            for line in inneroutput.readlines():
                if line.split(".")[-1][:-1] == extension:
                    suma += int(line.split(" ")[0])
            return suma

def printprojects(repos = repos, extensions = extensions):
    if os.path.exists("report_tmp"):
        os.remove("report_tmp")
    with open("report_tmp", "w") as report:
        for repo in repos:
            print repo
            first = True
            report.write("="*(30 - len(repo)/2) + " " + repo + " " + "="*(30 - len(repo)/2) + "\n")
            suma = 0
            for extension in extensions:
                count = countlines("../" + repo, extension)
                suma += count
                if (count != 0):
                    report.write( extension + ":" + " " + str(count) + ", ")
            report.write("\ntotal: " + str(suma) + "\n")
    os.rename("report_tmp", "report")

#print countlines("javatar", "java")

#print countlines("Django", "dupa")
#pull()
value = 0
while True:
    print value
    pull()
    printprojects()
    process = subprocess.Popen("sleep 60", shell = True)
    process.wait()
    value += 1

#pull()
#subprocess.call("wc " + filelist.readlines()[0], shell = True)
