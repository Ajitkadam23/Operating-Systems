#!/usr/bin/env python
# coding: utf-8

# In[301]:


#reading a file
file=open('C:/Users/admin/Downloads/sample inputfile1.txt','r')
f1=file.readlines()
ct=0

#     x.split(' ')
    
    

    
total_virtual_mem_size=0

size_of_process=[]
index_of_page_table=[]
previndex=0
# for i in range(no_of_process):
for x in f1:    
    
    index_of_page_table.append(previndex)
    total_virtual_mem_size=total_virtual_mem_size+int(x[2:])
#     print(x[2],total_virtual_mem_size)
    previndex=index_of_page_table[-1]+int(x[2:])/4+int(x[2:])%4
    size_of_process.append(x)
    ct=ct+1
no_of_process=ct
    
print(total_virtual_mem_size,index_of_page_table)
    
size_of_physical_mem=32
page_size=4
no_of_pageFrames=int(size_of_physical_mem/page_size)
Physical_mem=[[0,0,0] for i in range(no_of_pageFrames)]##[0,0,0]=processid,requiested page number,dirtybit
# Disc=[]

print(Physical_mem)



# In[302]:


#page_directory & page_tables
present_bit=0
frame_index=0
page_directory=[[present_bit,frame_index] for i in range(int(total_virtual_mem_size/4)+1)]


# In[303]:


#
index_of_available_page_frames=[i for i in range(int((size_of_physical_mem)/4))]

# def LRU(x,count_dict,qry):
#     mini=float('inf')
#     remove_this=float('inf')
#     for key,val in count_dict.items():
#         if val<mini:
#             mini=val
#             remove_this=key
#     index_of_page_frame=page_directory[int(remove_this)][1]
#     page_directory[int(remove_this)][0]=0
#     count_dict.pop(remove_this,None)
#     Physical_mem[index_of_page_frame]=[int(qry[0]),int(qry[2:]),0]
#     x[0]=1
#     x[1]=index_of_page_frame
#     count_dict[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])]+=1
    
    
    
        
    


# In[304]:


Qrfile=open('C:/Users/admin/Downloads/sample inputfile2.txt','r')
f2=Qrfile.readlines()
QueryArr=[]
for qry in f2:
    if qry=='\n':
        break
    QueryArr.append([int(qry[0]),int(qry[2:])])
print(QueryArr)


# In[305]:


size_of_TLB=int(size_of_physical_mem/2)
process_index=-1
process_offset=-1
page_frame_number=-1
TLB=[[process_index,process_offset,page_frame_number] for i in range(int(size_of_TLB/4))]
available_TLB_index=[i for i in range(int(size_of_TLB/4))]

page_frame_numer=-1
Hard_disc=[[page,page_frame_number] for page in range(int(total_virtual_mem_size/4)+4)]


def TLBOpti(x,ct,QueryARr,qry):
    pp=set()
    not_in_future=1
    for j in range(ct+1,len(QueryArr)):
        y=int(QueryArr[j][1]/4)+int(index_of_page_table[int(QueryArr[j][0])])
        if y in tb:
            
            if len(pp)==len(tb) -1:
                z=tb-pp
                not_in_future=0
                this_one=z.pop()
                tb.remove(this_one)
                page_frame_index=page_directory[this_one][1]
                break
            pp.add(y)
    if not_in_future==1:
        rd=tb-pp
#         print(tb,pp)
        this_one=rd.pop()
        page_frame_index=page_directory[this_one][1]
        tb.add(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])]))
        tb.remove(this_one)
        for i in range(len(TLB)):
            if index_of_page_table[int(TLB[i][0])]+int(int(TLB[i][1]))==int(this_one):
                TLB[i]=[int(qry[0]),int(int(qry[2:])/4),page_frame_index]
    else:
        tb.add(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])]))
        
        for i in range(len(TLB)):
            if index_of_page_table[int(TLB[i][0])]+int(int(TLB[i][1]))==int(this_one):
                
                TLB[i]=[int(qry[0]),int(int(qry[2:])/4),page_frame_index]
                   


# In[306]:


index_of_available_page_frames=[0,1,2,3,4,5,6,7]
def Optimal(x,ct,QueryArr,qry):
    p=set()
    not_in_future=1
    for j in range(ct+1,len(QueryArr)):
        y=int(QueryArr[j][1]/4)+int(index_of_page_table[int(QueryArr[j][0])])
        print('y',y)
        
        if y in S:
            
            if len(p)==len(S) -1:
                z=S-p
                not_in_future=0
                z=z.pop()
                this_one=z
                S.remove(z)
                print('z',z)
                page_frame_index=page_directory[z][1]
                break
            p.add(y)
    if not_in_future==1:
        rd=S-p
        this_one=rd.pop()
        page_frame_index=page_directory[this_one][1]
        S.add(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])]))
        Physical_mem[page_frame_index]=[int(qry[0]),int(qry[2:]),0]
        page_directory[page_frame_index][0]=0
        page_directory[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=1
        page_directory[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=page_frame_index
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=page_frame_index
        S.remove(this_one)
        replaced=0
        for kk in range(len(TLB)):
            if index_of_page_table[int(TLB[kk][0])]+int(int(TLB[kk][1]))==this_one:
                TLB[kk]=[int(qry[0]),int(int(qry[2:])/4),page_frame_index]
                replaced=1
                tb.add(page_frame_index)
        if replaced!=1:
        
            if len(available_TLB_index)!=0:

                TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),index_of_available_page_frames[0]]
                tb.add(index_of_page_directory)
            elif len(available_TLB_index)==0:
                TLBOpti(x,ct,QueryArr,qry)
    else:
        S.add(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])]))
        Physical_mem[page_frame_index]=[int(qry[0]),int(qry[2:]),0]
        page_directory[y][0]=0
        page_directory[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=1
        page_directory[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=page_frame_index
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=page_frame_index
                                                                                                       
                                                                                                        
        replaced=0
        for kk in range(len(TLB)):
            if index_of_page_table[int(TLB[kk][0])]+int(int(TLB[kk][1]))==this_one:
                TLB[kk]=[int(qry[0]),int(int(qry[2:])/4),page_frame_index]
                replaced=1
                tb.add(page_frame_index)
        if replaced!=1:
        
            if len(available_TLB_index)!=0:

                TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),index_of_available_page_frames[0]]
                tb.add(index_of_page_directory)
            elif len(available_TLB_index)==0:
                TLBOpti(x,ct,QueryArr,qry)

    
    
 
    
    
    


# In[307]:


Qrfile=open('C:/Users/admin/Downloads/sample inputfile2.txt','r')
f2=Qrfile.readlines()
count_dict={}
S=set()
tb=set()
ct=0
hit=0
for qry in f2:
#     print(page_directory)
    print(tb,TLB)
    ct=ct+1
    print(qry[0],qry[2:])
    if qry=='\n':
        break
    tlbhit=0
    index_of_page_directory=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
    for k in range(len(TLB)):
        if TLB[k][0]==int(qry[0]) and TLB[k][1]==int(int(qry[2:])/4):
#             print(count_dict_TLB,print(TLB))
# #             
#             count_dict_TLB[str(index_of_page_directory)]+=1
            Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
            Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=index_of_available_page_frames[0]
            tb.add(index_of_page_directory)
            hit=hit+1
            tlbhit=1
            print('TLB HIT and its TLB Hit No:',hit)
            break
    if tlbhit==1:
        continue
#     index_of_page_directory=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
   
    x=page_directory[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])]
    if x[0]==0 and len(index_of_available_page_frames)!=0:
        ###Bring from disc at next available index index_of_available_page_frames[0]
        print('page_fault_occurred')
        x[0]=1
        x[1]=index_of_available_page_frames[0]
#         print(Physical_mem)
        print(Physical_mem,index_of_available_page_frames[0])
        Physical_mem[index_of_available_page_frames[0]]=[int(qry[0]),int(qry[2:]),0]
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=index_of_available_page_frames[0]
       
#     
#         print(Physical_mem)
        index_of_available_page_frames.pop(0)
        S.add(index_of_page_directory)
        
        if len(available_TLB_index)!=0:
        
            TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),index_of_available_page_frames[0]]
            tb.add(index_of_page_directory)
        elif len(available_TLB_index)==0:
            TLBOpti(x,ct,QueryArr,qry)
    
    elif x[0]==1:
        print('page found in physical mem')
        if len(available_TLB_index)!=0:
        
            TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),x[1]]
            tb.add(index_of_page_directory)
        elif len(available_TLB_index)==0:
            TLBOpti(x,ct,QueryArr,qry)
        
    else:
        Optimal(x,ct,QueryArr,qry)
    
#     print(page_directory)
#     print(Physical_mem)
print(hit,ct)
print('TLB hit rate:', float(hit)/ct)
        
        
        
        
        


# In[308]:


print(Hard_disc)


# In[300]:


print(page_directory)


# In[ ]:




