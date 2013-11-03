from line_counter import *
value = 0
if not os.listdir("repos"):
    clone()
else:
    while True:
        print value
        pull()
        printprojects()
        process = subprocess.Popen("sleep 60", shell = True)
        process.wait()
        value += 1
