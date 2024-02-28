\ Model RAP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  53 assign[1,A] + 27 assign[1,B] + 13 assign[1,C] + 80 assign[2,A]
   + 47 assign[2,B] + 67 assign[2,C] + 53 assign[3,A] + 73 assign[3,B]
   + 47 assign[3,C]
Subject To
 task[A]: assign[1,A] + assign[2,A] + assign[3,A] = 1
 task[B]: assign[1,B] + assign[2,B] + assign[3,B] = 1
 task[C]: assign[1,C] + assign[2,C] + assign[3,C] = 1
 user[1]: assign[1,A] + assign[1,B] + assign[1,C] <= 1
 user[2]: assign[2,A] + assign[2,B] + assign[2,C] <= 1
 user[3]: assign[3,A] + assign[3,B] + assign[3,C] <= 1
Bounds
Generals
 assign[1,A] assign[1,B] assign[1,C] assign[2,A] assign[2,B] assign[2,C]
 assign[3,A] assign[3,B] assign[3,C]
End
