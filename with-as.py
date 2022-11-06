r = open('file.txt','a')
r.write('somthing' + '\n')
10 / 0
r.write('something more')
r.close()
print('It\'s all good')

# x = smth
# with *smth* as x: == try-with-resources in java: try(x = smth)
with open('file.txt','a') as r:
    r.write('somthing'+'\n')
    10/0
    r.write('something more')
print('It\'s all good')