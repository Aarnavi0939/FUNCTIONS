def swap_file_data():
    file1 = input("enter the first file name")
    file2 = input("enter the second file name")
    with open(file1,'r') as a:
        data1 = a.read()
    with open(file2,'r') as ab:
        data2 = ab.read()
    with open(file1,'w') as a:
        a.write(data2)
    with open(file2,'w') as ab:
        ab.write(data1)
swap_file_data()