import json,os,urllib.request,gc
gc.disable()
U=os.environ["MAKEFUN_ENV_URL"]
def P(p,b):
 r=urllib.request.Request(U+p,data=json.dumps(b).encode())
 with urllib.request.urlopen(r)as f:return json.load(f)
V=(0,100,320,330,500,900,100000)
D=(-17,-15,15,17);L=(-16,-1,1,16);K=(-17,-16,-15,-1,1,15,16,17);N=(-33,-31,-18,-14,14,18,31,33);R=(N,D,L,D+L,K)
class Z(Exception):pass
def F(f):
 b=[0]*128
 for i,r in enumerate(f.split()[0].split("/")):
  s=0
  for c in r:
   if c.isdigit():s+=int(c)
   else:b[(7-i)*16+s]=((c<"a")*2-1)*" pnbrqk".index(c.lower());s+=1
 return b
def A(b,s,c):
 if s<0:return 1
 for o in(D[:2]if c>0 else D[2:]):
  q=s+o
  if not q&0x88 and b[q]==c:return 1
 for O,v in(N,2),(K,6):
  for o in O:
   q=s+o
   if not q&0x88 and b[q]==v*c:return 1
 for O,T in((D,(3,5)),(L,(4,5))):
  for o in O:
   q=s+o
   while not q&0x88:
    if b[q]:
     if abs(b[q])in T and b[q]*c>0:return 1
     break
    q+=o
 return 0
def G(b,c,k=1):
 M=[]
 AP=M.append
 for s in SQ:
  p=b[s]
  if p*c<=0:continue
  a=abs(p)
  if a==1:
   f=16*c;q=s+f
   if not q&0x88 and not b[q]:
    if k or q>>4 in(0,7):AP((s,q))
    if k and s>>4==(1 if c>0 else 6)and not b[q+f]:AP((s,q+f))
   for o in(f-1,f+1):
    q=s+o
    if not q&0x88 and(b[q]*c<0 or q==b[8]>0):AP((s,q))
  else:
   for o in R[a-2]:
    q=s+o
    while not q&0x88:
     if b[q]:
      if b[q]*c<0:AP((s,q))
      break
     if k:AP((s,q))
     if a in(2,6):break
     q+=o
   if a==6 and s==(4 if c>0 else 116):
    for t,h in((6,7),(2,0))if c>0 else((118,119),(114,112)):
     if k and b[h]==4*c and not any(b[x]for x in range(min(s,h)+1,max(s,h)))and not A(b,s,-c)and not any(A(b,x,-c)for x in range(min(s,t)+1,max(s,t))):AP((s,t))
 return M
def W(b,f,t,c):
 p=b[f];b[8]=(t-16*c)if abs(p)==1 and t-f==32*c else 0;b[f]=0
 if abs(p)==1 and t!=f and not b[t]:b[t-16*c]=0
 b[t]=p
 if abs(p)==1 and t>>4 in(0,7):b[t]=5*c
 if abs(p)==6 and abs(f-t)==2:
  r=(7 if t>f else 0)+(f&112)
  b[t-1 if t>f else t+1]=b[r];b[r]=0
SQ=[q for q in range(128)if not q&0x88]
def Y(p,q):
 a=abs(p);f=q&7;r=q>>4
 if p<0:r=7-r
 g=V[a]
 if a==1:g+=r*12+4*(f in(3,4))
 elif a in(2,3,5):g+=9*(6-abs(2*f-7))+5*(6-abs(2*r-7))
 elif a==4:g+=15*(r==6)
 else:g+=12*(r<2)
 return g if p>0 else -g
E=[[0]*128 for _ in range(13)]
for p in range(-6,7):
 if p:
  for q in SQ:E[p+6][q]=Y(p,q)
def X(b):
 s=0
 for q in SQ:s+=E[b[q]+6][q]
 return s
NO=0;T=70000
def Q(b,a,z,c,kw,kb,h):
 global NO
 NO+=1
 if NO>T:raise Z
 s=X(b)*c
 if s>=z:return s
 if s>a:a=s
 if h>4:return a
 m=G(b,c,0)
 for f,t in sorted(m,key=lambda x:-abs(b[x[1]])):
  if b[t]and 1<abs(b[f])and s+V[abs(b[t])]<a:continue
  n=b[:];p=n[f];W(n,f,t,c)
  w,x=(kw,kb)if abs(p)>5 else((t,kb)if c>0 else(kw,t))
  v=-Q(n,-z,-a,-c,w,x,h+1)
  if v>=z:return v
  if v>a:a=v
 return a
def B(b,d,a,z,c,kw,kb,p):
 global NO
 NO+=1
 if NO>T:raise Z
 k=kw if c>0 else kb
 m=G(b,c)
 if not m:return A(b,k,-c)*(p-100000)
 if d<1:return Q(b,a,z,c,kw,kb,0)
 if d>3 and X(b)*c>=z and not A(b,k,-c)and-B(b,d-3,-z,-z+1,-c,kw,kb,p+1)>=z:return z
 s=-1000000
 for i,(f,t) in enumerate(sorted(m,key=lambda x:-abs(b[x[1]]))):
  n=b[:];p=n[f];W(n,f,t,c)
  w,x=(kw,kb)if abs(p)>5 else((t,kb)if c>0 else(kw,t))
  v=-B(n,d-1-(i>3 and not b[t]and d>2),-z,-a,-c,w,x,p+1)
  if v>s:s=v
  if s>a:a=s
  if a>=z:break
 return s
def S(b,d,c,kw,kb,ms):
 a=s=-1000000;best=ms[0][2]
 for f,t,u in ms:
  n=b[:];p=n[f];W(n,f,t,c)
  w,x=(kw,kb)if abs(p)>5 else((t,kb)if c>0 else(kw,t))
  v=-B(n,d-1,-1000000,-a,-c,w,x,1)
  if v>s:s=v;best=u
  if s>a:a=s
 return best
def choose(g):
 gc.collect()
 b=F(g["fen"]);c=1 if g["colour"]=="white"else-1
 kw=kb=-1
 for q in SQ:
  if b[q]==6:kw=q
  if b[q]==-6:kb=q
 ms=[]
 for u in g["legal_moves"]:
  if len(u)<5 or u[4]=="q":ms.append((ord(u[0])-97+(int(u[1])-1)*16,ord(u[2])-97+(int(u[3])-1)*16,u))
 global NO
 NO=0
 best=ms[0][2]
 for d in range(1,60):
  try:best=S(b,d,c,kw,kb,ms)
  except Z:break
 return best
while 1:
 g=P("/game",{})
 if g["status"][0]=="d":break
 while g["status"][0]=="y":
  g=P("/move",{"game":g["game"],"move":choose(g)})
