def func(file_path):
	f=open(file_path,'r'):
	nums=f.read()

	s=0
	for line in nums:
		s=s+int(line)

	return s