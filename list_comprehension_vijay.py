## This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# List comprehension
1.
sq = [n**2 for n in range(1,5)]
print('list of squares from 1 to 5 is',sq)
2.
num = [-3,-6,-75,78,35,-9,45,34,-287]
p = [n for n in num if n>0]
print('only positive numbers',p)
3.
num = [-3,-6,-75,78,35,-9,45,34,-287]
x = [n for n in num if n<0]
print('only negative numbers',x)
4.
even = [n for n in range(1,50) if n%2==0]
print('even numbers from 1 to 50',even)
5.
a = [n*5 for n in range(1,5)]
print('first 4 multiples of 5',a)
6.
names = ['anita','sunita','babita','mamta']
print([n.upper() for n in names])
7.
r = [3,45,76,8,90]
print([num+500 for num in r])
8.
e = [3,40,75,8,90]
print([[num,float (num)] for num in e])
9.
gender = ['B','G','B','B','G','G','B']
print(['BOY' if g=='B' else 'GIRL' for g in gender])
10.
text = 'my name is vijay'
v = [char for char in text if char in 'aeiou']
print('vowels in string',v)
11.
s = [2,5,-7,-4,9]
f = [n**2 if n>0 else abs(n) for n in s]
print('squares of positive numbers and absolute values of negative numbers',f)

