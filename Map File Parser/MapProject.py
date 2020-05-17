import sys
import re

def MapFun():
    sumText=0
    sumBss=0
    sumData=0
    sumRodata=0
    
    for j in sys.argv[1:]:
        f=open('Project_Memory_Map_File.map','r')
        f2=open(j+'_INFO.txt','w')
        s=f.read()
        match=re.findall(r'\w+\W(\w+)\s+\Wtext\s+'+j+'\w+\W+\w',s)
        for i in match:
            sizText=int(i,16)
            sumText=sumText+sizText
            
        match=re.findall(r'\w+\W(\w+)\s+\Wbss\s+'+j+'\w+\W+\w',s)
        for i in match:
            sizBss=int(i,16)
            sumBss=sumBss+sizBss
            
        match=re.findall(r'\w+\W(\w+)\s+\Wdata\s+'+j+'\w+\W+\w',s)
        for i in match:
            sizData=int(i,16)
            sumData=sumData+sizData
            
        match=re.findall(r'\w+\W(\w+)\s+\Wrodata\s+'+j+'\w+\W+\w',s)
        for i in match:
            sizRodata=int(i,16)
            sumRodata=sumRodata+sizRodata
        
        f2.write('            ***** '+j+' component Info *****\n\n')    
        f2.write(' Size of .text     section in '+j+' component is ='+str(sumText)+'Bytes\n')
        f2.write(' Size of .rodata   section in '+j+' component is ='+str(sumRodata)+'Bytes\n\n')
        f2.write(' Size of .data     section in '+j+' component is ='+str(sumData)+'Bytes\n')
        f2.write(' Size of .bss      section in '+j+' component is ='+str(sumBss)+'Bytes\n\n')
        f2.write('-> Size of ROM in '+j+' component is ='+str(sumText+sumRodata)+'Bytes\n')
        f2.write('-> Size of RAM in '+j+' component is ='+str(sumData+sumBss)+'Bytes\n')
        
        
     




def main():
    MapFun()
    
if __name__ == '__main__':
    main()