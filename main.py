# birinchi vazifa
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in list1:
    if i%3==0:
     print(i)
# ikkinchi vazifa
rel=0
for i in range(1,6,1):
    son=int(input(f'{i} soni kiriting'))
    rel=rel+son
print(rel)
# uchinchi vazifa
text=(input('matn kiriting: '))
for e in  text:
   if e in 'aueio':
    print(e)
# tortinchi vazifa
faktorial=1
son=int(input('soni kiriting:'))
for i in range(1,son+1,1):
  faktorial*=i
print(faktorial)
# beshinchi vazifa
list=[-1,2,45,10,11,45,-15]
for i in list:
   if i>0:
      print(i)
