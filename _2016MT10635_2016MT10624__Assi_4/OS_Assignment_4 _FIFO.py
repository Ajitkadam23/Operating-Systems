#!/usr/bin/env python
# coding: utf-8

# In[166]:


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



# In[167]:


#page_directory & page_tables
present_bit=0
frame_index=0
page_directory=[[present_bit,frame_index] for i in range(int(total_virtual_mem_size/4)+1)]


# In[168]:


#query conversion 


# query=input()
# page_directory[query[1]%4+[index_of_page_table[query[0]]]]##starting index of that process in page directory+offset part
size_of_TLB=int(size_of_physical_mem/2)
process_index=-1
process_offset=-1
page_frame_number=-1
TLB=[[process_index,process_offset,page_frame_number] for i in range(int(size_of_TLB/4))]
Hard_disc=[[page,page_frame_number] for page in range(int(total_virtual_mem_size/4)+4)]


def FIFOTLB(TLB,x,index):
    newstack=[]
    l=len(TLB)
    while l>0:
        newstack.append(TLB.pop())
        l=l-1
    put_on_hd=newstack.pop()
    m=len(newstack)
    while m>0:
        TLB.append(newstack.pop())
        m=m-1
    TLB.append([int(qry[0]),int(qry[2:]),index])
        
    
    


# In[169]:


#
index_of_available_page_frames=[i for i in range(int(size_of_physical_mem/4))]
available_TLB_index=[i for i in range(int(size_of_TLB/4))]

def FIFO(x):
#     if Physical_mem[0][2]==1:
        ###write changes on hdd??
#     Physical_mem[0]=[[qry[0],qry[1],0]]
    newstack=[]
    l=len(Physical_mem)
    while l>0:
        newstack.append(Physical_mem.pop())
        l=l-1
    put_on_hd=newstack.pop()
    m=len(newstack)
    while m>0:
        Physical_mem.append(newstack.pop())
        m=m-1
    Physical_mem.append([int(qry[0]),int(qry[2:]),0])
        
    x[0]=1
    x[1]=len(Physical_mem)
    Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
    Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=len(Physical_mem)
       
    if len(available_TLB_index)!=0:
            TLB[available_TLB_index.pop(0)]=[[int(qry[0]),int(qry[2:]),index_of_available_page_frames[0]]]
    elif len(available_TLB_index)==0:
            FIFOTLB(TLB,x,len(Physical_mem))
    


# In[170]:


Qrfile=open('C:/Users/admin/Downloads/sample inputfile2.txt','r')
f2=Qrfile.readlines()
hit=0
ct=0
for qry in f2:
#     print(page_directory)
    print(qry[0],qry[2:])
    if qry=='\n':
        break
    tlbhit=0
    for k in range(len(TLB)):
        if TLB[k][0]==int(qry[0]) and TLB[k][1]==int(int(qry[2:])/4):
            hit=hit+1
            tlbhit=1
            print('TLB HIT and its TLB Hit No:',hit)
            break
    print(TLB)
    if tlbhit==1:
        continue
#     print('ITS TLB MISS')
    
    x=page_directory[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])]
    if x[0]==0 and len(index_of_available_page_frames)!=0:
        ###Bring from disc at next available index index_of_available_page_frames[0]
        print('Its TLB miss with page_fault')
        x[0]=1
        x[1]=index_of_available_page_frames[0]
#         print(Physical_mem)
        
        Physical_mem[index_of_available_page_frames[0]]=[int(qry[0]),int(qry[2]),0]
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=index_of_available_page_frames[0]
       
        if len(available_TLB_index)!=0:
            TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),index_of_available_page_frames[0]]
        elif len(available_TLB_index)==0:
            FIFOTLB(TLB,x,x[1])
#         print(Physical_mem)
        index_of_available_page_frames.pop(0)
    elif x[0]==1:
        print('Its TLB Miss with page  in physical mem')
        if len(available_TLB_index)!=0:
            TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),index_of_available_page_frames[0]]
        elif len(available_TLB_index)==0:
            FIFOTLB(TLB,x,x[1])
    else:
        print('Its TLB miss with page_fault')
        FIFO(x)
    ct=ct+1
    
print('final hit TLB hit rate:',float(hit)/ct)
#     print(page_directory)
#     print(Physical_mem)
    
        
        
        
        
        


# In[171]:


print(Physical_mem)
    
    


# In[16]:


##LRU


# In[ ]:




