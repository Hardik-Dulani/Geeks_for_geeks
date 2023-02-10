# Bob is very fond of balloons. Once he visited an amusement park with his mother. 
# The mother told Bob that she would buy him a balloon only if he answer her problem right. 
# She gave Bob a string S [contains only lowercase characters] and 
# asked him to use the characters of string to form as many instances of the word "balloon" as possible. 
# Return the maximum number of instances that can be formed.

# Help Bob to solve the problem.

# Note: You can use each character in the string at most once.

  
  
def maxInstance(self, s : str) -> int:
    b= "balon"
    ins= []
    correct = [1,1,2,2,1]
    for i in b:
        a = s.count(i)
        ins.append(a)
    mini = min(ins)
    res = [ins[i]//correct[i] for i in range(5) if ins[i]/correct[i]>=1]
    if len(res)==5:
        return min(res)

    return 0
