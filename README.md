# cserializabilitychecker
Program builds the precedence graph for given schedule and specifies whether it is "Conflict Serializable" or Not.

Input Format :

Enter the operations seperated by comma or spaces such that for every operation: 
-First character specifies operation type (r for read or w for write) 
-Second character specifies the Transaction ID (1-9) 
-Third character specifies the variable on which that operation is done

Sample Input:
r1x w2x w3x r1x w1x r4x r4y

Output:
  Precedence Graph Plot highlighting cycle (if any exists)
