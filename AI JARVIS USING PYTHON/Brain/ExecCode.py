import subprocess

def ExecCode(code:str):
    code = "from Functions.Tools.ImgGen import Generate_Images\nfrom Body.Speak import speak\n"+code
    code = code.replace("print", "speak")

    with open(r"temp.py", "w") as f:
        f.write(code)
    
    subprocess.getoutput("python temp.py 2> error.log")

    with open(r"error.log", "r") as f:
        res = f.read()
        if res != "":
            return False
        else:
            return True