# You have been given an array A of size N consisting of positive integers. 
# You need to find and print the product of all the number in this array Modulo 10^9 +7.

# Input Format:
# The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

# Output Format:
# Print a single integer denoting the product of all the elements of the array Modulo 10^9 +7.

# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/



def find_product(input_list):
    i = 0
    answer = 1
    while i < len(input_list):
        answer = (answer * int(input_list[i])) % (10**9 + 7)
        i+= 1

    print (answer)
list_size = input()
input_list = list(map(int,input().split()))

find_product(input_list)
        