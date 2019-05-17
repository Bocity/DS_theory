lis = []
know1 = [0.9,0.1]
know2 = [0.8,0.05]
print("输入流鼻涕事实概率:")
l = float(input().strip())
lis.append(l)
print("输入眼发炎事实概率:")
l = float(input().strip())
lis.append(l)
print("h1:感冒但非过敏性鼻炎\nh2:过敏性鼻炎但非感冒\nh3:同时得了两种病")
m1 = []
m2 = []
for i in range(2):
    print("M1({{h{}}})={}x{}={}".format(i + 1,lis[0],know1[i],lis[0]*know1[i]))
    m1.append(lis[0]*know1[i])
print("M1({{h1,h2,h3}}) = 1 - M1({{h1}}) - M1({{h2}}) = 1 - {} - {} = {}".format(m1[0],m1[1],1 - m1[0] - m1[1]))
m1.append(1 - m1[0] - m1[1]) 
for i in range(2):
    print("M2({{h{}}})={}x{}={}".format(i + 1,lis[1],know2[i],lis[1]*know2[i]))
    m2.append(lis[1]*know2[i])
print("M2({{h1,h2,h3}}) = 1 - M2({{h1}}) - M2({{h2}}) = 1 - {} - {} = {}".format(m2[0],m2[1],1 - m2[0] - m2[1]))
m2.append(1 - m2[0] - m2[1])
print("K={}".format(1.0 / (1 - m1[0]*m2[1] - m1[1]*m2[0])))
k = 1.0 / (1 - m1[0]*m2[1] - m1[1]*m2[0])
m = []
print("M({{h1}}) = {}".format(k*(m1[0]*m2[0]+m1[0]*m2[2]+m1[2]*m2[0])))
m.append(k*(m1[0]*m2[0]+m1[0]*m2[2]+m1[2]*m2[0]))
print("M({{h2}}) = {}".format(k*(m1[1]*m2[1]+m1[1]*m2[2]+m1[2]*m2[1])))
m.append(k*(m1[1]*m2[1]+m1[1]*m2[2]+m1[2]*m2[1]))
bel = []
pl = []
for i in range(2):
    print("Bel({{h{}}}) = {}".format(i + 1,m[i]))
    bel.append(m[i])
for i in range(2):
    print("Pl({{h{}}}) = {}".format(i + 1, 1 - (m[0]+m[1]-m[i])))
    pl.append(1 - (m[0]+m[1]-m[i]))
print("感冒的信任程度:[{},{}]".format(bel[0],pl[0])) 
print("过敏性鼻炎的信任程度:[{},{}]".format(bel[1],pl[1]))

    
    
