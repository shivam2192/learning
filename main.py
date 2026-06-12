def main():
    arr = [1,2,3,4,-5,6,2,6]
    Sub = 3
    sub_sum_main = 0
    #print(len(arr)-Sub)
    for i in range(0,len(arr)-1):
        sub_sum = 0
        if (i<=len(arr)-Sub):
            for j in range(i,i+Sub):
                sub_sum = sub_sum + arr[j]
           # print(sub_sum)
        if( sub_sum_main < sub_sum):
            sub_sum_main = sub_sum
    print(sub_sum_main)

def second_approch():
    arr = [1,2,3,4,-5,6,2,6]
    Sub = 3
    sub_sum =0
    sub_sum_main =0
    
    #print(len(arr)-Sub)
    for i in range(len(arr)-Sub):
        sub_sum =0
        sub_sum = sub_sum + sum(range(arr[i],arr[i-Sub+1]))
        if(sub_sum>sub_sum_main):
            sub_sum_main=sub_sum
    
    print(sub_sum_main)

# find the longest palindrome in sub string 
def palindrome():
    s = "ababab"
    if s == s[::-1]:
        print("palindrome")
    sub_str_compare =''
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1]:
                if len(sub_str) > len(sub_str_compare):
                    sub_str_compare = sub_str 
    print(sub_str_compare)


if __name__ == "__main__":
    palindrome()
