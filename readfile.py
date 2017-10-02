with open("Crime.csv",'r') as file:
 mainlist=[]
 list2=[]
 count=[]
 i=0 
 j=1
 k=2
 countvalue=0
 for line in file:
  line.strip()
  line.split(",")
  print(line)
"""
  if line[2] in mainlist:
   mainlist.index(line[7])
   count[index]+=1
   list2[k]=count[index]
  else:
   list1.append(line[7])
   list2[i]=list[8]
   list2[j]=list[7]
   count.append(1)
   list2[k]=count[index1]
   i+=3
   j+=3
   k+=3
"""
