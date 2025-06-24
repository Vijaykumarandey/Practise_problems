s1 = "they are round"
s2 = "fold two times"
def shadow(s1,s2):
    a1 = s1.split(" ")
    a2 = s2.split(" ")
    if len(a1) != len(a2):
       return False
    else:
        for i in range(len(a1)):
           if len(a1[i]) != len(a2[i]):
               return False
        return True
print(shadow(s1,s2))