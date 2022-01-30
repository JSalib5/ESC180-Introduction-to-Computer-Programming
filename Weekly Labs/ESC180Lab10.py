#problem 1
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * (power(x, n-1))

#problem 2
def interleave(L1, L2):
    if len(L1) == 0:
        return L1
    else:
        return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

#problem 3
def reverse_rec(L):
    if len(L) == 0:
        return L
    else:
        return [L.pop(-1)] + reverse_rec(L)

#problem 4
def zigzag1(L):
    if len(L) == 0:
        return L
    else:
        print(L.pop(int(len(L)/2 - 0.5)))
        return zigzag1(L)

#problem 5
def is_balanced(s):
    if not "(" in s and not ")" in s:
        return True
    if  not "(" in s or not ")" in s:
        return False
    else:
        if s.find("(") < s.find(")"):
            s = s.replace("(", "",1)
            s = s.replace(")", "",1)
            return is_balanced(s)
        else:
            return False

if __name__ == '__main__':
    string1 = "(()(()))"
    string2 = "(well (I think), recursion works like that (as far as I know)"
    string3 = "(()(())"
    string4 = "(well (I think)), recursion works like that ((as far as I know))()()"
    L1 = ["A", "B", "C", "D", "E"]
    L2 = [1, 2, 3]
    L3 = ["A", "B", "C"]

    print(power(2, 4))
    print(interleave(L2, L3))
    print(reverse_rec(L3))
    print(zigzag1(L1))
    print(is_balanced(string3))