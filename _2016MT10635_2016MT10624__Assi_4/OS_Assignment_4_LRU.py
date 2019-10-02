#!/usr/bin/env python
# coding: utf-8

# In[132]:


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



# In[133]:


#page_directory & page_tables
present_bit=0
frame_index=0
page_directory=[[present_bit,frame_index] for i in range(int(total_virtual_mem_size/4)+1)]


# In[134]:


size_of_TLB=int(size_of_physical_mem/2)
process_index=-1
process_offset=-1
page_frame_number=-1
TLB=[[process_index,process_offset,page_frame_number] for i in range(int(size_of_TLB/4))]

def LRUTLB(x,count_dict_TLB,qry):
    mini=float('inf')
    remove_this=float('inf')
    print(count_dict_TLB,TLB)
    for key,val in count_dict_TLB.items():
        if val<mini:
            mini=val
            remove_this=key
    
    index_of_page_frame=page_directory[int(remove_this)][1]
    count_dict_TLB.pop(remove_this,None)
    print(count_dict_TLB)
    if str(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])) not in count_dict_TLB:
        count_dict_TLB[str(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])]))]=1
    else:
        count_dict_TLB[str(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])]))]= count_dict_TLB[str(int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])]))]+1
    print(count_dict_TLB)
            
    for i in range(len(TLB)):
        if index_of_page_table[int(TLB[i][0])]+int(int(TLB[i][1])) ==int(remove_this):
            TLB[i]=[int(qry[0]),int(int(qry[2:])/4),index_of_page_frame]
            break
    
    
    


# In[135]:


#
index_of_available_page_frames=[0,1,2,3,4,5,6,7]
available_TLB_index=[i for i in range(int(size_of_TLB/4))]
Hard_disc=[[page,page_frame_number] for page in range(int(total_virtual_mem_size/4)+4)]



def LRU(x,count_dict,qry):
    mini=float('inf')
    remove_this=float('inf')
    for key,val in count_dict.items():
        if val<mini:
            mini=val
            remove_this=key
    index_of_page_frame=page_directory[int(remove_this)][1]
    page_directory[int(remove_this)][0]=0
    count_dict.pop(remove_this,None)
    Physical_mem[index_of_page_frame]=[int(qry[0]),int(qry[2:]),0]
    x[0]=1
    x[1]=index_of_page_frame
#     count_dict[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])]+=1
    if len(available_TLB_index)!=0:
        for j in range(len(TLB)):
            if int(remove_this)==index_of_page_table[int(TLB[j][0])]+int(int(TLB[j][1])/4):
#                 available_TLB_index.append(j)
                TLB[j][0]=-1
                TLB[j][1]=-1

                TLB[j]=[int(qry[0]),int(int(qry[2:])/4),index_of_page_frames]
    elif len(available_TLB_index)==0:
        LRUTLB(x,count_dict_TLB,qry)
    
            
        
    
    
    
        
    


# In[136]:


Qrfile=open('C:/Users/admin/Downloads/sample inputfile2.txt','r')
f2=Qrfile.readlines()
count_dict={}
count_dict_TLB={}
ct=0
hit=0
for qry in f2:
#     print(page_directory)
#     print(count_dict_TLB,TLB)
    print(qry[0],qry[2:])
    ct=ct+1
    if qry=='\n':
        break
    index_of_page_directory=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])

    tlbhit=0
    for k in range(len(TLB)):
        if TLB[k][0]==int(qry[0]) and TLB[k][1]==int(int(qry[2:])/4):
            print(count_dict_TLB,print(TLB))
#             
            count_dict_TLB[str(index_of_page_directory)]+=1
            
            hit=hit+1
            tlbhit=1
            print('TLB HIT and its TLB Hit No:',hit)
            break
    if tlbhit==1:
        continue
    if str(index_of_page_directory) not in count_dict:
        
        count_dict[str(index_of_page_directory)]=1
    else:
        count_dict[str(index_of_page_directory)]+=1
    x=page_directory[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])]
    if x[0]==0 and len(index_of_available_page_frames)!=0:
        ###Bring from disc at next available index index_of_available_page_frames[0]
        print('page_fault_occurred')
        x[0]=1
        x[1]=index_of_available_page_frames[0]
#         print(Physical_mem)
        Physical_mem[index_of_available_page_frames[0]]=[int(qry[0]),int(qry[2:]),0]
#         print(Physical_mem)   
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][0]=int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])
        Hard_disc[int(int(qry[2:])/4)+int(index_of_page_table[int(qry[0])])][1]=index_of_available_page_frames[0]
       
        if len(available_TLB_index)!=0:
        
            TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),index_of_available_page_frames[0]]
            if str(index_of_page_directory) not in count_dict_TLB:
                
        
                count_dict_TLB[str(index_of_page_directory)]=1
            else:
                count_dict_TLB[str(index_of_page_directory)]+=1
        elif len(available_TLB_index)==0:
            LRUTLB(x,count_dict_TLB,qry)
        index_of_available_page_frames.pop(0)
    elif x[0]==1:
        if str(index_of_page_directory) not in count_dict_TLB:
        
            count_dict_TLB[str(index_of_page_directory)]=1
        else:
            count_dict_TLB[str(index_of_page_directory)]+=1
        if len(available_TLB_index)!=0:
            TLB[available_TLB_index.pop(0)]=[int(qry[0]),int(int(qry[2:])/4),x[1]]
        elif len(available_TLB_index)==0:
            LRUTLB(x,count_dict_TLB,qry)
        print('page found in physical mem')
        
    else:
        LRU(x,count_dict,qry)
#     print(page_directory)
#     print(Physical_mem)

print('Hit rate:',float(hit)/ct)
        
        
        
        


# In[64]:


print(Physical_mem)
index_of_available_page_frames
print(count_dict)


# In[25]:





# In[ ]:




