def tower_hanoi(n,a,b,c):
    if n==1:
        print("move lst disk from", a,"to ",c)
        return
    tower_hanoi(n-1,a,c,b)
    print("move",n,"th  disk from", a,"to ",c)
    tower_hanoi(n-1,b,a,c)
tower_hanoi(4,"s","h","d")
    
  """
  move lst disk from s to  h
move 2 th  disk from s to  d
move lst disk from h to  d
move 3 th  disk from s to  h
move lst disk from d to  s
move 2 th  disk from d to  h
move lst disk from s to  h
move 4 th  disk from s to  d
move lst disk from h to  d
move 2 th  disk from h to  s
move lst disk from d to  s
move 3 th  disk from h to  d
move lst disk from s to  h
move 2 th  disk from s to  d
move lst disk from h to  d"""
