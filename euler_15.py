
#http://blog.sina.com.cn/s/blog_79aae9bd0101kcwq.html
def init_list():
    d0 = []
    for i in range(1,22):
        #for j in range(1,22):
        d0.append ( [0]*22)
    return d0

d1 = init_list()
print d1


for i in range(21):
    for j in range(21):
        d1[i][0]=1
        d1[0][j]=1
        d1[0][0]=0

print d1

for i in range(21):
    for j in range(21):
        d1[i][j] = d1[i-1][j] + d1[i][j-1]

print d1[20][20]