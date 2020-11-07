import webbrowser as wb
import os
import getpass
print("=============================WELCOME TO MY AWS CLI WORLD===============================")


print("Before using this program make sure you have aws software installed and have access key and secret key to access your aws IAM account")
print("To use AWS services please configure your AWS instance.")
print("configure aws")
os.system("aws configure")


while True:
	
	print("""
	Press 0: To exit
	Press 1: To launch a new instance
	Press 2: To see list of all the instances
	Press 3: To stop instance
	Press 4: To start existing instance
	Press 5: To create key-pair
	Press 6: To create security group
	Press 7: To create EBS volume
	Press 8: To attach EBS volume to instance
	Press 9: To create S3 bucket
	Press 10: To upload image in S3 bucket
	Press 11: To change the bucket permission 
	Press 12: To create Cloudfront web distribution
	""")

	ch = input("Enter your choice: ")
	print(ch)

	if int(ch) == 0:
		exit()
	
	elif int(ch) == 1:
		img_id = input("Enter image id: ")
		inst_type = input("Enter instance type: ")
		sub_id = input("Enter subnet id: ")
		sg_id = input("Enter security group's id: ")
		key = input("Enter key name: ")
		os.system("aws ec2 run-instances --image-id {} --instance-type {} --subnet-id {} --security-group-id {} --key-name {} --count 1".format(img_id,inst_type,sub_id,sg_id,key))
		
	elif int(ch) == 2:
		os.system("aws ec2 describe-instances")

	elif int(ch) == 3:
		i_id = input("Enter the instance id which you want to stop: ")
		os.system("aws ec2 stop-instances --instance-ids {}".format(i_id))

	elif int(ch) == 4:
		in_id = input("Enter instance id which you want to start: ")
		os.system("aws ec2 start-instances --instance-ids {}".format(in_id))

	elif int(ch) == 5:
		k_name = input("Enter the key name: ")
		os.system("aws ec2 create-key-pair --key-name {}".format(k_name))

	elif int(ch) == 6:
		g_name = input("Enter security group name eg.,MysecurityGroup: ")
		d = input("Enter description of security group eg.,MySecurityGroup: ")
		os.system("aws ec2 create-security-group --group-name {} --description {}".format(g_name,d))

	elif int(ch) == 7:
		v_type = input("Enter volume type: ")
		s = input("Enter size of volume eg.,1 : ")
		av_zone = input("Enter name of availability zone: ")
		os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(v_type,s,av_zone))

	elif int(ch) == 8:
		print("Before attaching EBS volume to an instance make sure your EBS volume and instance are in the same availability zone")
		de = input("Enter device eg.,/dev/sda : ")
		v_id = input("Enter volume id: ")
		i_id = input("Enter instance id: ")
		os.system("aws ec2 attach-volume --device {} --volume-id {} --instance-id {}".format(de,v_id,i_id))

	elif int(ch) == 9:
		b_name = input("Enter name of bucket: ")
		r = input("Enter region where you want to create bucket: ")
		b_cfg = input("Enter bucket configuration eg.,LocationConstraint=ap-south-1 : ")
		os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration {}".format(b_name,r,b_cfg))

	elif int(ch) == 10:
		img_path = input("Enter the complete path of the image you want to upload: ")
		b_name = input("Enter name of the bucket: ")
		os.system("aws s3 sync \"{}\" s3\:\/\/{}\ ".format(img_path,b_name))

	elif int(ch) == 11:
		b_name = input("Enter bucket name: ")
		img_name = input("Enter image file name: ")
		permission = input("Enter permission you want to give eg.,public-read: ")
		os.system("aws s3api put-object-acl --bucket {} --key {} --acl {}".format(b_name,img_name,permission))

	elif int(ch) == 12:
		b_name = input("Enter bucket name: ")
		os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws".format(b_name))

	else:
		print("Invalid choice")
		exit()