Subsequence is a sub-array, 
which has all the numbers part of main array and in same order, 
but may not be at same index. Similarly Reverse Sub Array will be same as sub array but index in reverse Order. 

Design a Method:
================

def IsSubArray(Main:[],Sequence:[]):
	pass

Result can be following:
========================

- Sequence is Sub Array of Main Array
- Sequence is Reverse Sub Array of Main Array
- Sequence is Bi-directional Sub Array of Main Array
- Sequence is not a Sub Array of Main Array

for eg:

==============================
MainArray = [6,3,5,1,7,4,9]
==============================

Sub = [6,7,9] - Yes its a Sub Array as 6,7,9 is in main array and in same sequence (Sequence is Sub Array of Main Array)
Sub = [3,1,4] - Yes its a Sub Array as 3,1,4 is in main array and in same sequence (Sequence is Sub Array of Main Array)

Sub = [9,7,5] - Yes its a Reverse Sub Array as 9,7,5 is in main array and in reverse sequence (Sequence is Reverse Sub Array of Main Array)

Sub = [7,9,5] - Its neither Sub Array or Reverse (Sequence is not a Sub Array of Main Array

Sub = [9,13,12] - Its neither, since elements are missing from main array (Sequence is not a Sub Array of Main Array)

===========================
Main Array = [3,3,3,3,3]
===========================

Sub = [3,3,3] - Qualify as both Sub Array and Reverse Sub Array (Sequence is Bi-directional Sub Array of Main Array)

Sub = [3,3,3,3,3,3] - Doesn't qualify as either, since Sub array is bigger than Main array (Sequence is not a Sub Array of Main Array)
