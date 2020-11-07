import os
import getpass
import webbrowser as wb

os.system("tput setaf 3")
print("\t\t\t Welcome to the World of Automation !!")
os.system("tput setaf 7")
print("\t\t\t-------------------------------------------")

password = getpass.getpass("Enter your password: ")

if password != "ARTHbyLW":
	print("Password incorrect!!!")
	exit()

def l_name_core():
	l_ip = input("Enter Hadoop name node ip : ")
	print(l_ip)
	os.system("echo \<configuration\> >> core-site.xml")
	os.system("echo \<property\> >> core-site.xml")
	os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
	os.system("echo \<value\>hdfs:\/\/{}:9001\<\/value\> >> core-site.xml".format(l_ip))
	os.system("echo \<\/property\> >> core-site.xml")
	os.system("echo \<\/configuration\> >> core-site.xml")
	os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(l_ip))
	os.system("rm -rf core-site.xml")
	os.system("cp cp.xml core-site.xml")

def r_name_core():
	r_ip = input("Enter Hadoop name node ip : ")
	print(r_ip)
	os.system("echo \<configuration\> >> core-site.xml")
	os.system("echo \<property\> >> core-site.xml")
	os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
	os.system("echo \<value\>hdfs:\/\/{}:9001\<\/value\> >> core-site.xml".format(r_ip))
	os.system("echo \<\/property\> >> core-site.xml")
	os.system("echo \<\/configuration\> >> core-site.xml")
	os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(r_ip))
	os.system("rm -rf core-site.xml")
	os.system("cp cp.xml core-site.xml")

def l_data_core():
	l_nn_ip = input("Enter NameNode ip :")
	print(l_nn_ip)
	l_dn_ip = input("Enter Datanode ip : ")
	print(l_dn_ip)
	os.system("echo \<configuration\> >> core-site.xml")
	os.system("echo \<property\> >> core-site.xml")
	os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
	os.system("echo \<value\>hdfs:\/\/{}:9001\<\/value\> >> core-site.xml".format(l_nn_ip))
	os.system("echo \<\/property\> >> core-site.xml")
	os.system("echo \<\/configuration\> >> core-site.xml")
	os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(l_dn_ip))
	os.system("rm -rf core-site.xml")
	os.system("cp cp.xml core-site.xml")

def r_data_core():
	r_nn_ip = input("Enter NameNode ip :")
	print(r_nn_ip)
	r_dn_ip = input("Enter Datanode ip : ")
	print(r_dn_ip)
	os.system("echo \<configuration\> >> core-site.xml")
	os.system("echo \<property\> >> core-site.xml")
	os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
	os.system("echo \<value\>hdfs:\/\/{}:9001\<\/value\> >> core-site.xml".format(r_nn_ip))
	os.system("echo \<\/property\> >> core-site.xml")
	os.system("echo \<\/configuration\> >> core-site.xml")
	os.system("scp core-site.xml {}:/etc/hadoop/core-site.xml".format(r_ip))
	os.system("rm -rf core-site.xml")
	os.system("cp cp.xml core-site.xml")

def l_name_hdfs():
	l_nn_dir = input("Enter directory name you want to create for namenode:")
	print(l_nn_dir)

	os.system("echo \<configuration\> >> hdfs-site.xml")
	os.system("echo \<property\> >> hdfs-site.xml")
	os.system("echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml")
	os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(l_nn_dir))
	os.system("echo \<\/property\> >> hdfs-site.xml")
	os.system("echo \<\/configuration\> >> hdfs-site.xml")
    	
	os.system("mkdir {}".format(l_nn_dir))
	os.system("rm -rf hdfs-site.xml")
	os.system("cp hd.xml hdfs-site.xml")

def r_name_hdfs():
	r_nn_dir = input("Enter directory name you want to create for namenode:")
	print(r_nn_dir)

	os.system("echo \<configuration\> >> hdfs-site.xml")
	os.system("echo \<property\> >> hdfs-site.xml")
	os.system("echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml")
	os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(r_nn_dir))
	os.system("echo \<\/property\> >> hdfs-site.xml")
	os.system("echo \<\/configuration\> >> hdfs-site.xml")
    	
	os.system("ssh {} mkdir {}".format(r_ip,l_nn_dir))
	os.system("rm -rf hdfs-site.xml")
	os.system("cp hd.xml hdfs-site.xml")

def l_data_hdfs():
	l_dn_dir = input("Enter directory name you want to create for datanode:")
	print(l_dn_dir)

	os.system("echo \<configuration\> >> hdfs-site.xml")
	os.system("echo \<property\> >> hdfs-site.xml")
	os.system("echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml")
	os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(l_dn_dir))
	os.system("echo \<\/property\> >> hdfs-site.xml")
	os.system("echo \<\/configuration\> >> hdfs-site.xml")
    	
	os.system("mkdir {}".format(l_dn_dir))
	os.system("rm -rf hdfs-site.xml")
	os.system("cp hd.xml hdfs-site.xml")

def r_data_hdfs():
	r_dn_dir = input("Enter directory name you want to create for datanode:")
	print(r_dn_dir)

	os.system("echo \<configuration\> >> hdfs-site.xml")
	os.system("echo \<property\> >> hdfs-site.xml")
	os.system("echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml")
	os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(r_dn_dir))
	os.system("echo \<\/property\> >> hdfs-site.xml")
	os.system("echo \<\/configuration\> >> hdfs-site.xml")
    	
	os.system("ssh {} mkdir {}".format(r_ip,r_dn_dir))
	os.system("rm -rf hdfs-site.xml")
	os.system("cp hd.xml hdfs-site.xml")


def l_namenode():
	j_h_dir = print("Enter the directory name where Java and Hadoop files resides : ") 
	print(j_h_dir)
	os.system("rpm -i {}/jdk-8u171-linux-x64.rpm".format(j_h_dir))
	os.system("rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm".format(j_h_dir))
	l_name_core()
	l_name_hdfs()
	os.system("hadoop namenode -format")
	os.system("hadoop-daemon.sh start namenode")
	os.system("jps")

def r_namenode():
	j_h_dir = print("Enter the directory name where Java and Hadoop files resides : ") 
	print(j_h_dir)
	os.system("ssh {} rpm -i {}/jdk-8u171-linux-x64.rpm".format(r_ip,j_h_dir))
	os.system("ssh {} rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm".format(r_ip,j_h_dir))
	r_name_core()
	r_name_hdfs()
	os.system("ssh {} hadoop namenode -format".format(r_ip))
	os.system("ssh {} hadoop-daemon.sh start namenode".format(r_ip))
	os.system("ssh {} jps".format(r_ip))

def l_datanode():
	j_h_dir = print("Enter the directory name where Java and Hadoop files resides : ") 
	print(j_h_dir)
	os.system("rpm -i {}/jdk-8u171-linux-x64.rpm".format(j_h_dir))
	os.system("rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm".format(j_h_dir))
	l_data_core()
	l_data_hdfs()
	os.system("hadoop-daemon.sh start datanode")
	os.system("jps")

def r_datanode():
	j_h_dir = print("Enter the directory name where Java and Hadoop files resides : ") 
	print(j_h_dir)
	os.system("ssh {} rpm -i {}/jdk-8u171-linux-x64.rpm".format(r_ip,j_h_dir))
	os.system("ssh {} rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm".format(r_ip,j_h_dir))
	r_data_core()
	r_data_hdfs()
	os.system("ssh {} hadoop-daemon.sh start datanode".format(r_ip))
	os.system("ssh {} jps".format(r_ip))

def l_unmount():
    dvd_loc = input("Enter location where ur dvd was mounted")
    os.system("umount /dev/cdrom {}".format(dvd_loc))

def r_unmount():
    dvd_loc1 = input('Enter location where ur dvd was mounted')
    os.system('ssh {} umount /dev/cdrom {}'.format(r_ip,dvd_loc1))

def l_yum():
	l_repo_name = input("Enter folder_name/repo_name u want to mount to :")
	print("Before using this tool make sure your dvd is not mounted if mounted then use option 15 and then configure yum")
	os.system("mkdir \/{}".format(l_repo_name))
	os.system("mount \/dev\/cdrom \/{}".format(l_repo_name))
	os.system("touch \/etc\/yum.repos.d\/{}\.repo".format(l_repo_name))
	os.system("echo \[dvd\] \>\> \/etc\/yum.repos.d\/{}.repo".format(l_repo_name))
	os.system("echo baseurl\=file\\\:\/\/{}\/BaseOS \>\> \/etc\/yum.repos.d\/{}.repo".format(l_repo_name,l_repo_name))
	os.system("echo gpgcheck\=0 \>\> \/etc\/yum.repos.d\/{}.repo".format(l_repo_name))
	os.system("echo \[dvd1\] \>\> \/etc\/yum.repos.d\/{}.repo".format(l_repo_name))
	os.system("echo baseurl\=file\\\:\/\/{}\/AppStream \>\> \/etc\/yum.repos.d\/{}.repo".format(l_repo_name,l_repo_name))
	os.system("echo gpgcheck \= 0 \>\> \/etc\/yum.repos.d\/{}.repo".format(l_repo_name))
	os.system("echo mount \/dev\/cdrom {} \>\> \/etc\/rc.d\/rc.local".format(l_repo_name))
	os.system("chmod +x \/etc\/rc.d\/rc.local")
	os.system("yum clean all")
	os.system("yum repolist")

def r_yum():
	r_repo_name = input("Enter folder_name/repo_name u want to mount to :")
	print("Before using this tool make sure your dvd is not mounted if it is mounted then use our 15th option then configure yum")
	os.system("ssh {} mkdir \/{}".format(r_ip,r_repo_name))
	os.system("ssh {} mount \/dev\/cdrom \/dvd".format(r_ip))
	os.system("ssh {} touch \/etc\/yum.repos.d\/{}\.repo".format(r_ip,r_repo_name))
	os.system("ssh {} echo \[dvd\] \>\> \/etc\/yum.repos.d\/dvd.repo".format(r_ip))
	os.system("ssh {} echo baseurl\=file\\\:\/\/{}\/BaseOS \>\> \/etc\/yum.repos.d\/dvd.repo".format(r_ip,r_repo_name))
	os.system("ssh {} echo gpgcheck\=0 \>\> \/etc\/yum.repos.d\/dvd.repo".format(r_ip))
	os.system("ssh {} echo \[dvd1\] \>\> \/etc\/yum.repos.d\/dvd.repo".format(r_ip))
	os.system("ssh {} echo baseurl\=file\\\:\/\/{}\/AppStream \>\> \/etc\/yum.repos.d\/dvd.repo".format(r_ip,r_repo_name))
	os.system("ssh {} echo gpgcheck \= 0 \>\> \/etc\/yum.repos.d\/dvd.repo".format(r_ip))
	os.system("ssh {} echo mount \/dev\/cdrom {} \>\> \/etc\/rc.d\/rc.local".format(r_ip,r_repo_name))
	os.system("ssh {} chmod +x \/etc\/rc.d\/rc.local".format(r_ip))
	os.system("ssh {} yum clean all".format(r_ip))
	os.system("ssh {} yum repolist".format(r_ip))

def l_docker():
	print("Before configuring docker make sure your yum is configured if not choose option 11 first then configure docker")
	os.system("sudo yum config\-manager \-\-add\-repo\=https\:\/\/download.docker.com\/linux\/centos\/docker\-ce\.repo")
	os.system("dnf install docker-ce --nobest -y")
	os.system("systemctl start docker")
	os.system("systemctl enable docker")
	os.system("systemctl status docker")

def r_docker():
	print("Before configuring docker make sure your yum is configured if not choose option 11 first then configure docker")
	os.system("ssh {} sudo yum config\-manager \-\-add\-repo\=https\:\/\/download.docker.com\/linux\/centos\/docker\-ce\.repo".format(r_ip))
	os.system("ssh {} dnf install docker-ce --nobest -y".format(r_ip))
	os.system("ssh {} systemctl start docker".format(r_ip))
	os.system("ssh {} systemctl enable docker".format(r_ip))
	os.system("ssh {} systemctl status docker".format(r_ip))

def l_d_webserver():
	print("Before configuring webserver make sure your yum is configured otherwise go to option 11 first")
	l_ip = input("Enter the ip of docker os:")
	p = int(input("Enter port :"))
	os_name = input("Enter OS name:")
	img_name = input("Enter image name with version:")
	file_name = ("Enter file name which you want to  run over webserver : ")
	os.system("docker run -it --name {} -p {}:80 {}".format(os_name,p,img_name))
	os.system("docker exec -i {} yum install httpd -y".format(os_name))
	os.system("docker cp {} {}:\/var\/www\/html".format(file_name))
	os.system("docker exec -i {} /usr/sbin/httpd".format(os_name))
	os.system("curl http\:\/\/{}\:{}".format(l_ip,p))

def r_d_webserver():
	print("Before configuring webserver make sure your yum is configured otherwise go to option 11 first")
	p = int(input("Enter port :"))
	os_name = input("Enter OS name:")
	img_name = input("Enter image name with version:")
	file_name = input("Enter file name which you want to run over webserver : ")
	os.system("ssh {}docker run -it --name {} -p {}:80 {}".format(r_ip,os_name,p,img_name))
	os.system("ssh {} docker exec -i {} yum install httpd -y".format(r_ip,os_name))
	os.system("ssh {} docker cp {} {}:\/var\/www\/html".format(r_ip,file_name))
	os.system("ssh {} docker exec -i {} /usr/sbin/httpd".format(r_ip,os_name))
	os.system("curl http\:\/\/{}\:{}".format(r_ip,p))

def l_webserver():
	print("Before configuring webserver make sure your yum is configured if not choose option 11 first")
	l_ip = ("Enter the ip of local system: ")
	print(l_ip)
	os.system("yum install httpd -y")
	os.system("systemctl start httpd")
	os.system("systemctl enable httpd")
	os.system("systemctl status httpd")
	os.system("echo Automation \>\> \/var\/www\/html\/auto.html")
	os.system("curl -I http\:\/\/{}\/auto.html".format(l_ip))

def r_webserver():
	print("Before configuring webserver make sure your yum is configured if not choose option 11 first")
	os.system("ssh {} yum install httpd -y".format(r_ip))
	os.system("ssh {} systemctl start httpd".format(r_ip))
	os.system("ssh {} systemctl enable httpd".format(r_ip))
	os.system("ssh {} systemctl status httpd".format(r_ip))
	os.system("ssh {} echo Automation \>\> \/var\/www\/html\/auto.html".format(r_ip))
	os.system("curl -I http\:\/\/{}\/auto.html".format(r_ip))


def l_ansible():
	print("Make sure before installing you have installed Python")
	os.system("pip3 install ansible")
	os.system("touch ip.txt")
	ip = input("Enter the IP address of target node: ")
	user = input("Enter the username of target node: ")
	password = input("Enter the password of target node: ")
	protocol = input("Enter the connection protocol for target node: ")
	os.system("echo {} ansible_user={} ansible_ssh_pass={} ansible_connection={}".format(ip,user,password,protocol))
	os.system("mkdir \/etc\/ansible")
	os.system("touch \/etc\/ansible\/ansible.cfg")
	os.system("echo \[defaults\] \>\> \/etc\/ansible\/ansible.cfg")
	os.system("echo inventory = \/root\/ip.txt \>\> \/etc\/ansible\/ansible.cfg")
	os.system("echo host_key_checking = false \>\> \/etc\/ansible\/ansible.cfg")
	os.system("dnf install https:\/\/dl.fedoraproject.org\/pub\/epel-release-latest-8.noarch.rpm")
	os.system("yum install sshpass")
	print("Your ansible control node configured successfully!!")

def r_ansible():
	print("Make sure before installing you have installed Python")
	os.system("ssh {} pip3 install ansible".format(r_ip))
	os.system("ssh {} touch ip.txt".format(r_ip))
	ip = input("Enter the IP address of target node: ")
	user = input("Enter the username of target node: ")
	password = input("Enter the password of target node: ")
	protocol = input("Enter the connection protocol for target node: ")
	os.system("ssh {} echo {} ansible_user={} ansible_ssh_pass={} ansible_connection={}".format(r_ip,ip,user,password,protocol))
	os.system("ssh {} mkdir \/etc\/ansible".format(r_ip))
	os.system("ssh {} touch \/etc\/ansible\/ansible.cfg".format(r_ip))
	os.system("ssh {} echo \[defaults\] \>\> \/etc\/ansible\/ansible.cfg".format(r_ip))
	os.system("ssh {} echo inventory = \/root\/ip.txt \>\> \/etc\/ansible\/ansible.cfg".format(r_ip))
	os.system("ssh {} echo host_key_checking = false \>\> \/etc\/ansible\/ansible.cfg".format(r_ip))
	os.system("ssh {} dnf install https\:\/\/dl.fedoraproject.org\/pub\/epel-release-latest-8.noarch.rpm".format(r_ip))
	os.system("ssh {} yum install sshpass".format(r_ip))
	print("Your ansible control node configured successfully!!")

def l_ansible_webserver():
	print("Make sure your yum is configured before configuring webserver using ansible")
	l_ip = input("Enter the ip of local system: ")
	os.system("ansible all -m package -a \"name=httpd state=present\" ")
	f_name = input("Enter name of html file you want to copy from control node to target node: ")
	os.system("ansible all -m copy -a \"src={} dest=\/var\/www\/html\"".format(f_name))
	os.system("ansible all -m service -a \'name=httpd state=started\" ")
	os.system("curl -I http\:\/\/{}\/{}".format(l_ip,f_name))

def r_ansible_webserver():
	print("Make sure your yum is configured before configuring webserver using ansible")
	os.system("ssh {} ansible all -m package -a \"name=httpd state=present\" ".format(r_ip))
	f_name = input("Enter name of html file you want to copy from control node to target node: ")
	os.system("ssh {} ansible all -m copy -a \"src={} dest=\/var\/www\/html\"".format(r_ip,f_name))
	os.system("ssh {} ansible all -m service -a \"name=httpd state=started\" ".format(r_ip))
	os.system("curl -I http\:\/\/{}\/{}".format(r_ip,f_name))

r = input("Where you want to run this program ? (local/remote) : ")
print(r)

while True:
	
	print("""
	Press 1: Date
	Press 2: Calender
	Press 3: Create file
	Press 4: Create directory/folder
	Press 5: To check network connectivity
	Press 6: To see the list of directories
	Press 7: To see present working directory
	Press 8: To configure hadoop Name_node
	Press 9: To configure hadoop Data_node
	Press 10: To configure yum
	Press 11: To configure docker
	Press 12: To configure webserver in docker
	Press 13: To configure webserver in Base OS
	Press 14: To unmount dvd
	Press 15: To see all the present Disks and partitions
	Press 16: To see partitions inside any particular disk
	Press 17: To create physical volume
	Press 18: To display physical volume
	Press 19: To create volume group
	Press 20: To display volume group
	Press 21: To create logical volume
	Press 22: To display logical volume
	Press 23: To format disk or logical group
	Press 24: To mount the partition
	Press 25: To create static partition
	Press 26: To increase the size of logical volume
	Press 27: To reduce the size of logical volume
	Press 28: To resize the logica volume
	Press 29: To configure Ansible
	Press 30: To configure webserver using Ansible
	Press 31: To exit
        """)

	ch = input("Enter your choice : " )
	print(ch)

	if r == "local":
		

		if int(ch) == 1:
			os.system("date")
		elif int(ch) == 2:
			os.system("cal")
		elif int(ch) == 3:
			fi = input("Enter file name you want to create : ")
			os.system("touch {}".format(fi))
			print("Your file is created")
		elif int(ch) == 4:
			dir = input("Enter directory name you want to create : ")
			os.system("mkdir {}".format(dir))
			print("Your directory is created")
		elif int(ch) == 5:
			p_ip = input("Enter the ip you want to ping")
			os.system("ping -c 4 {}".format(p_ip))
		elif int(ch) == 6:
			os.system("ls")
		elif int(ch) == 7:
			os.system("pwd")
		elif int(ch) == 8:
			l_namenode()
		elif int(ch) == 9:
			l_datanode()
		elif int(ch) == 10:
			l_yum()
		elif int(ch) == 11:
			l_docker()
		elif int(ch) == 12:
			l_d_webserver()
		elif int(ch) == 13:
			l_webserver()
		elif int(ch) == 14:
			l_unmount
		elif int(ch) == 15:
			os.system("fdisk -l")
		elif int(ch) == 16:
			drive = input("Enter the name of the drive: ")
			os.system("fdisk {} -l".format(drive))
		elif int(ch) == 17:
			disk = input("Enter name of the disk you want to convert to physical volume: ")
			os.system("pvcreate {}".format(disk))
		elif int(ch) == 18:
			d = input("Enter disk name: ")
			os.system("pvdisplay {}".format(d))
		elif int(ch) == 19:
			vg_name = input("Enter name of the volume group: ")
			di = input("Enter the name of the disk you want to add to volume group: ")
			os.system("vgcreate {} {}".format(vg_name,di))
		elif int(ch) == 20:
			vg = input("Enter the name of the volume group you want to see: ")
			os.system("vgdisplay {}".format(vg))
		elif int(ch) == 21:
			s = input("Enter the size of the volume like 10G,5M : ")
			l = input("Enter the name of the logical volume: ")
			v = input("Enter the name of the volume group: ")
			os.system("lvcreate --size {} --name {} {}".format(s,l,v))
		elif int(ch) == 22:
			lv = input("Enter the name of the logical volume eg., /dvd/vg_name/lv_name : ")
			os.system("lvdisplay {}".format(lv))
		elif int(ch) == 23: 
			d = input("Enter the name of disk or logical group you want to format: ")
			os.system("mkfs.ext4 {}".format(d))
		elif int(ch) == 24:
			dest = input("Enter the name of the destination where you want to mount the partition: ")
			dis = input("Enter the name of the disk or logical volume you want to mount: ")
			os.system("mount {} {}".format(dis,dest))
		elif int(ch) == 25:
			os.system("fdisk -l")
			disk = ("Enter the name of the disk: ")
			os.system("fdisk {}".format(disk))
			os.system("mkfs.ext4 {}".format(disk))
			os.system("udevadm settle")
			desti = input("Enter the name of the destination directory where youn want to mount the partition: ")
			os.system("mount {} {}".format(disk,desti))
		elif int(ch) == 26:
			size = input("Enter the size you want to increase eg., 10G : ")
			lv = input("Enter the name of the logical volume: ")
			os.system("lvextend --size +{} {}".format(size,lv))
		elif int(ch) == 27:
			s = input("Enter the size you want to reduce eg., 10G : ")
			l_v = input("Enter the name of the logical volume: ")
			os.system("lvreduce -L {} {}".format(s,l_v))
		elif int(ch) == 28:
			n = input("Enter the name of the logical volume eg., /dev/iiec/lw : ")
			os.system("resize2fs {}".format(n))
			os.system("df -h")
		elif int(ch) == 29:
			l_ansible()
		elif int(ch) == 30:
			l_ansible_webserver()
		elif int(ch) == 31:
			exit()
		else:
			print("Invalid choice")
			exit()
	

	else:
		r_ip = input("Enter remote ip: ")
		print(r_ip)

		if int(ch) == 1:
			os.system("ssh {} date".format(r_ip))
		elif int(ch) == 2:
			os.system("ssh {} cal".format(r_ip))
		elif int(ch) == 3:
			fi = input("Enter file name you want to create : ")
			os.system("ssh {} touch {}".format(r_ip,fi))
			print("Your file is created")
		elif int(ch) == 4:
			dir = input("Enter directory name you want to create : ")
			os.system("ssh {} mkdir {}".format(r_ip,dir))
			print("Your directory is created")
		elif int(ch) == 5:
			p_ip = input("Enter the ip you want to ping")		
			os.system("ssh {} ping -c 4 {}".format(r_ip,p_ip))
		elif int(ch) == 6:
			os.system("ssh {} ls".format(r_ip))
		elif int(ch) == 7:
			os.system("ssh {} pwd".format(r_ip))
		elif int(ch) == 8:
			r_namenode()
		elif int(ch) == 9:
			r_datanode()
		elif int(ch) == 10:
			r_yum()
		elif int(ch) == 11:
			r_docker()
		elif int(ch) == 12:
			r_d_webserver()
		elif int(ch) == 13:
			r_webserver()
		elif int(ch) == 14:
			r_unmount
		elif int(ch) == 15:
			os.system("ssh {} fdisk -l".format(r_ip))
		elif int(ch) == 16:
			drive = input("Enter the name of the drive: ")
			os.system("ssh {} fdisk {} -l".format(r_ip,drive))
		elif int(ch) == 17:
			disk = input("Enter name of the disk you want to convert to physical volume: ")
			os.system("ssh {} pvcreate {}".format(r_ip,disk))
		elif int(ch) == 18:
			d = input("Enter disk name: ")
			os.system("ssh {} pvdisplay {}".format(r_ip,d))
		elif int(ch) == 19:
			vg_name = input("Enter name of the volume group: ")
			di = input("Enter the name of the disk you want to add to volume group: ")
			os.system("ssh {} vgcreate {} {}".format(r_ip,vg_name,di))
		elif int(ch) == 20:
			vg = input("Enter the name of the volume group you want to see: ")
			os.system("ssh {} vgdisplay {}".format(r_ip,vg))
		elif int(ch) == 21:
			s = input("Enter the size of the volume like 10G,5M : ")
			l = input("Enter the name of the logical volume: ")
			v = input("Enter the name of the volume group: ")
			os.system("ssh {} lvcreate --size {} --name {} {}".format(r_ip,s,l,v))
		elif int(ch) == 22:
			lv = input("Enter the name of the logical volume eg., /dvd/vg_name/lv_name : ")
			os.system("ssh {} lvdisplay {}".format(r_ip,lv))
		elif int(ch) == 23: 
			d = input("Enter the name of disk or logical group you want to format: ")
			os.system("ssh {} mkfs.ext4 {}".format(r_ip,d))
		elif int(ch) == 24:
			dest = input("Enter the name of the destination where you want to mount the partition: ")
			dis = input("Enter the name of the disk or logical volume you want to mount: ")
			os.system("ssh {} mount {} {}".format(r_ip,dis,dest))
		elif int(ch) == 25:
			os.system("ssh {} fdisk -l".format(r_ip))
			disk = ("Enter the name of the disk: ")
			os.system("ssh {} fdisk {}".format(r_ip,disk))
			os.system("ssh {} mkfs.ext4 {}".format(r_ip,disk))
			os.system("ssh {} udevadm settle".format(r_ip))
			desti = input("Enter the name of the destination directory where youn want to mount the partition: ")
			os.system("ssh {} mount {} {}".format(r_ip,disk,desti))
		elif int(ch) == 26:
			size = input("Enter the size you want to increase eg., 10G : ")
			lv = input("Enter the name of the logical volume: ")
			os.system("ssh {} lvextend --size +{} {}".format(r_ip,size,lv))
		elif int(ch) == 27:
			s = input("Enter the size you want to reduce eg., 10G : ")
			l_v = input("Enter the name of the logical volume: ")
			os.system("ssh {} lvreduce -L {} {}".format(r_ip,s,l_v))
		elif int(ch) == 28:
			n = input("Enter the name of the logical volume eg., /dev/iiec/lw : ")
			os.system("ssh {} resize2fs {}".format(r_ip,n))
			os.system("df -h")
		elif int(ch) == 29:
			r_ansible()
		elif int(ch) == 30:
			r_ansible_webserver()
		elif int(ch) == 31:
			exit()
		else:
			print("Invalid choice")
			exit()

else:
	print("Not supported login")	
	input("\n Please enter to continue")


			
