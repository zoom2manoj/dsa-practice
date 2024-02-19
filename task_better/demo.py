
def openfile_write(filename):
    file = open(filename, "w")
    return file

def writefile(file, data):
    file.write(data)
    file.write('\n')

def fileclose(file):
    file.close()


def readfile(filename):
    with open(filename, 'r') as reader:
        data = reader.readlines()
        return data

def exact_data(filename):
    data = readfile(filename)
    return [x.rstrip() for x in data]

filename = 'input.txt'
result_file = 'output.txt'
data_task = exact_data(filename)

index=0
file = openfile_write(result_file)
while index<len(data_task):
    x = data_task[index]
    if ')' in x:
        task_count = data_task[index+1]
        task_row = data_task[index + 2:index + 2 + int(task_count)]
        for i in range(len(task_row)):
            task = task_row[i]
            task = task.split(';')
            # task[0]
            print("task t{0} have input data sources {1} and output data sources {2}".format( i, task[0], task[1]))
        initial_data = data_task[index+2+int(task_count)]
        output = initial_data.split(',')
        output= [x, str(int(output[0])-1),',', str(int(output[len(output)-1])-1)]
        output = ''.join(output)
        writefile(file, output)
        index = index + 3 + int(task_count)

fileclose(file)


