# cserializabilitychecker
Program builds the precedence graph for given schedule and specifies whether it is "Conflict Serializable" or Not.

Input Format :

Enter the operations seperated by comma or spaces such that for every operation: 
-First character specifies operation type (r for read or w for write) 
-Second character specifies the Transaction ID (1-9) 
-Third character specifies the variable on which that operation is done

Sample Inputs:
r1x r2z r1z r3y r3y w1x w3y r2y w2z w2y
r1x w2x w3x r1x
r1x w2x w3x r1x w1x r4x r4y
r1x r2x w2x w1x r3x

Output:
  Precedence Graph Plot highlighting cycle (if any exists)
