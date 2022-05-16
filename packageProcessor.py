f=open('./stream-response.txt')
data = f.readline()
data = data.split('&') # 'sfzhux': '1'
strList = []
for item in data:
    temp = item.split('=')
    temp_str = "\'" + temp[0] + "\': \'" + temp[1] + "\'"
    print(temp_str)
