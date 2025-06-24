'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def find_blocking_spot(pos1, pos2):
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for line in winning_lines:
        if pos1 in line and pos2 in line:
            third = [pos for pos in line if pos != pos1 and pos != pos2]
            if third:
                return third[0]
    
    return "not in list" 
a = int(input())
b = int(input())
print(find_blocking_spot(a,b))  
