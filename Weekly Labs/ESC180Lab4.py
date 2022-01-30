import math

#Problem 1
def count_events(L):
  counter = 0
  for i in range(0, len(L)):
    if L[i] % 2 == 0:
      counter += 1
  return counter

#Problem 2
def list_to_str(lis):
  strlis = ""
  for i in range(0, len(lis) - 1):
    strlis += str(lis[i]) + ", "
  strlis = "[" + strlis + str(lis[len(lis) - 1]) + "]"
  return strlis

#Problem 3
def lists_are_the_same(list1, list2):
  check = True

  if len(list1) != len(list2):
    check = False

  for i in range (len(list1)):
    if list1[i] != list2[i]:
      check = False
  return check

#Problem 4
def simplify_fraction(n, m):
  fraction = ""
  for i in range(max(n, m) , 2, -1):
    if n % i == 0 and m % i == 0:
      n /= i
      m /= i
  fraction = str(int(n)) + "/" + str(int(m))
  return fraction

#Problem 5
def Leibiniz_Formula(n):
    sum = 0
    for i in range(0, n+1):
        sum += ((-1)**i)/(2*i+1)
    sum = sum * 4
    return sum

def check_pi(n):
  x = math.pi
  pi_approx = int(x*(10**(n-1)))
  terms = 1

  while int(Leibiniz_Formula(terms)*(10**(n-1))) != pi_approx:
      terms += 1
      if int(Leibiniz_Formula(terms)*(10**(n-1))) == pi_approx:
          return terms


#Problem 6
def simplify_fraction2(b, a):
  global steps1
  steps1 = 0
  for i in range(max(b, a) , 2, -1):
    steps1 += 1
    if b % i == 0 and a % i == 0:
      b /= i
      a /= i
  return steps1

def euc_alg(b, a):
  c, d = a, b
  if d < c:
    c, d = d, c
  while c != 0:
    d, c = c, d%c
  gcd = c
  fraction = str(int(b/gcd)) + "/" + str(int(a/gcd))
  return fraction


def euc_alg2(b, a):
  global steps2
  c, d, steps2 = a, b, 0
  if d >= c:
    R = d % c
    while R != 0:
      d = c
      c = R
      R = d % c
      steps2 += 1
    steps2 += 2
  return steps2

def fraction_comparison(a, b):
  simplify_fraction2(b, a)
  euc_alg2(b, a)
  if steps1 > steps2:
    print("Euclidian Algorithim is more efficient")
  elif steps2 > steps1:
    print("Naive Algorithim is more efficient")


if __name__ == "__main__":
  List = [2, 3, 4, 5, 7, 9, 12, 13, 2]
  List1 = [1, 2, 3]
  List2 = [1, 2, 3]
  Num1 = 8
  Num2 = 12

  #Problem 1
  print(count_events(List))

  #Problem 2
  print(list_to_str(List))

  #Problem 3
  print(lists_are_the_same(List1, List2))

  #Problem 4
  print(simplify_fraction(Num1, Num2))

  #Problem 5
  print(check_pi(3))

  #Problem 6
  print(fraction_comparison(24353, 562))
  print(euc_alg(24353, 562))