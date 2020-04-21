import os
import time
os.system("clear")
os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("pkg install python3 -y")
os.system("pkg install python2 -y")
os.system("pkg install python -y")
os.system("pkg install php -y")
os.system("pkg install git -y ")
os.system("pkg install python-pip git -y")
os.system("pkg install speedtest-cli -y")
os.system("clear")
x=("python3 ttool.py")
print ("""
  __                                        __                .__
_/  |_  ___________  _____  __ _____  ___ _/  |_  ____   ____ |  |   ______
\   __\/ __ \_  __ \/     \|  |  \  \/  / \   __\/  _ \ /  _ \|  |  /  ___/
 |  | \  ___/|  | \/  Y Y  \  |  />    <   |  | (  <_> |  <_> )  |__\___ \
 |__|  \___  >__|  |__|_|  /____//__/\_ \  |__|  \____/ \____/|____/____  >
           \/            \/            \/                               \/
""")
print("""
1-weeman
2-Red Hawk
3-Tmux-Bunch
4-sqlmap
5-Striker
6-Optiva-framework
7-metasploit
8-fake call
9-WPSeku
10-Enternet speed test

99- exit
""")
a=int(input("Ttools > "))
if (a==1) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/samyoyo/weeman")
    time.sleep(2)
    os.system(x)
elif (a==2) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("  git clone https://github.com/Tuhinshubhra/RED_HAWK")
    time.sleep(2)
    os.system(x)
elif (a==3) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/Hax4us/Tmux-Bunch.git")
    time.sleep(2)
    os.system(x)
elif (a==4) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/sqlmapproject/sqlmap")
    time.sleep(2)
    os.system(x)
elif (a==5) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/UltimateHackers/Striker && cd Striker && pip install -r requirements.txt")
    time.sleep(2)
    os.system(x)
elif (a==6) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/joker25000/Optiva-Framework")
    time.sleep(2)
    os.system(x)
elif (a==7) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/verluchie/termux-metasploit && chmod 777 termux-metasploit/install.sh && bainstall gitsh termux-metasploit/install.sh &&")
    time.sleep(2)
    os.system(x)
elif (a==8) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/siputra12/fakecall.git")
    time.sleep(2)
    os.system(x)
elif (a==9) :
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")
    os.system("git clone https://github.com/m4ll0k/WPSeku.git && cd wpseku && pip3 install -r requirements.txt")
    time.sleep(2)
    os.system(x)
elif (a==10) :
    os.system("speedtest-cli")
    time.sleep(2)
    os.system(x)

else :
    print ("exiting ...,")
    print ('''
\033[1;33m         [ + ] \033[1;32mThanks for using termux-tools
\033[1;33m         [ + ] \033[1;32mGood By..... :)\033[00m''')
    time.sleep(5)
    os.system("clear")
