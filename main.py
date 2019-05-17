import os
import sys



def stage2(site):

    path="/etc/nginx/sites-available/default"
    f=open(path,"r").read()
    f=f.replace("default_server","")
    a="/var/www/{}/html".format(site)
    f=f.replace("/var/www/html",a)
    a="server_name {} www.{};".format(site,site)
    f=f.replace("server_name _;",a)
    path=path="/etc/nginx/sites-available/{}".format(site)
    g=open(path,"w")
    g.write(f)
    g.close()
    print("[+] Sucessfully Created the configuration file for {}".format(site))
    task="ln -s /etc/nginx/sites-available/{} /etc/nginx/sites-enabled/".format(site)
    if os.system(task)==0:
        print("[+] Successfully created the symlinks")
        path="/var/www/{}/html/index.html".format(site)
        cmd="echo '<h1>Hello this is {}</h1>' > {}".format(site,path)
        os.system(cmd)
        os.system("systemctl restart nginx")
        print("NOW OPEN THE SITE SIRE :) http://{}".format(site))
    else:
        print("Error Symlinking")


if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
else:
    e=input("Enter the sitename with domain ex:- 'google.com':-")
    ss="which nginx"
    if os.system(ss)==0:
        cmd="bash main.sh {}".format(e)
        os.system(cmd)
        stage2(e)
    else:
        cmd="bash main.sh {}".format(e)
        os.system(cmd)
        print("\nWe are installing the nginx please run this script again after installation")
        sys.exit()
