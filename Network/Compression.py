import zipfile
zip_file = zipfile.ZipFile('brothers.zip', 'w')
zip_file.write('brothers.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()

with open('brothers.txt', encoding='utf-8') as f:
	lines = [line for line in f.readlines()]
	chars = [char for line in lines for char in line]
	words = [word for line in lines for word in line.split()]



