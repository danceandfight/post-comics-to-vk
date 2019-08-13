import tempfile

def wrt_file():
	with open('tst.txt', 'w') as f:
		f.write('First line!')
	return f

print(wrt_file())