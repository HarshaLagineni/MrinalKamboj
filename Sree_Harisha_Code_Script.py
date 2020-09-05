'''
Name : Sree Harisha
Date : 05-09-2020
Description :

Result can be following:
========================

- Sequence is Sub Array of Main Array
- Sequence is Reverse Sub Array of Main Array
- Sequence is Bi-directional Sub Array of Main Array
- Sequence is not a Sub Array of Main Array

'''

######################################################################################################
#1. isSubArray(MainArray, Sub, n, m):  to check main sub and sub are matching sequence are not.
def isSubArray(MainArray, Sub, n, m): 
      
    # Two pointers arrays 
    i = 0; j = 0; 
  
    # Traverse both arrays simultaneously 
    while (i < n and j < m): 
  
        # If element matches 
        if (MainArray[i] == Sub[j]): 
  
            i += 1; 
            j += 1; 
  
            # If array B is completely 
            # traversed 
            if (j == m): 
                return True; 
          
        # If not, 
        # increment i and reset j 
        else: 
            i = i - j + 1; 
            j = 0; 
          
    return False; 
  
# Driver Code 
if __name__ == '__main__': 
    MainArray = [6,3,5,1,7,4,9]; 
    n = len(MainArray); 
    Sub = [6,7,9]; 
    m = len(Sub); 
  
    if (isSubArray(MainArray, Sub, n, m)): 
        print("YES"); 
    else: 
        print("NO"); 
######################################################################################################
###Other way fo executing the given requirement 
def IsSubArray(Main,Sequence):
        if len(Sequence)>len(Main):
                return "subarray is greater than main array"
        index=[]
        for i in Sequence:
                try:
                        ind=Main.index(i)
                        index.append(ind)
                except:
                        return "Sequence is not subbarray of main array"
        fcount=0
        for i in range(0,len(index)):
                if i==len(index)-1:
                        continue
                if index[i]<index[i+1]:
                        pass
                else:
                        fcount=fcount+1
        if fcount==0:
                return "sequence is subarray of main array"
        rcount=0
        for i in reversed(range(len(index))):
                if i==0:
                        continue
                if index[i]<index[i-1]:
                        pass
                else:
                        rcount=rcount+1
        if rcount==0:
                return "sequence is reverse subarray of main array"

        if fcount>0 or rcount >0:
                return "it is neither sub array or reverse sequence is not a sub array of main array"

main=[6,3,5,1,7,4,9]
#Sequence is Sub Array of Main Array
sub=[6,7,9]
print(IsSubArray(main,sub))

#Sequence is Reverse Sub Array of Main Array 
sub=[9,7,5]
print(IsSubArray(main,sub))

#Sequence is Reverse Sub Array of Main Array
sub=[7,9,5]
print(IsSubArray(main,sub))

#Sequence is not a Sub Array of Main Array
sub=[7,9,99]
print(IsSubArray(main,sub))


######################################################################################################
#subarray is a slice from the array which is contiguous elements
def IsSubArray(MainArray):
    for i in range(len(MainArray)):
        for j in range(i,len(MainArray)):
            print(MainArray[i: j+1])

if __name__ == '__main__':
    MainArray = [6,3,5,1,7,4,9]
    IsSubArray(MainArray)


######################################################################################################
#Sub = [3,3,3] - Qualify as both Sub Array and Reverse Sub Array (Sequence is Bi-directional Sub Array of Main Array)
arr = [3,3,3,3,3]
print("Array is :",arr)

res = arr[::-1]
print('Sub Array and reversed Sub array:',res[:3])

######################################################################################################

#Sub = [3,3,3] - Qualify as both Sub Array and Reverse Sub Array (Sequence is Bi-directional Sub Array of Main Array)

def IsSubArray(Main,Sequence):
    if len(Sequence)==len(Main):
        return "Doesn't qualify as either, since Sub array is bigger than Main array "
    else:
        return 'Both are same length'

MainArray = [3,3,3,3,3]
Sub = [3,3,3,3,3,3]

IsSubArray(MainArray,  Sub )      


