import socket                   # Import socket module
import os.path
def pullf():
	host="172.16.144.193"
	s=socket.socket()
	s.connect((host,6000))
	path=os.getenv("HOME")
	
	'''for host in hosts:
		try:
			s.connect((host,6000))
		except:
			continue'''
	s.send(b'a')
	x=s.recv(1024)
	filename=repr(x)
	save_path=path+"/dgit"+"/originalfiles"+"/"+filename
	with open(save_path,'wb') as f:
		print("file opened")
		while True:
			data=s.recv(1024)
			if not data:
					break
			f.write(data)
	f.close()
	print("successfuly get the file")
	s.close()
	print("connection closed")
	paths=os.getenv("HOME")
	dirname=paths+'/dgit/'+filename;
	a=str(os.path.exists(dirname))
	if(a=='False'):		
			os.mkdir(dirname)
			f = open(os.path.join(dirname, 'record.txt'), 'w')
			f.close()
				
	
