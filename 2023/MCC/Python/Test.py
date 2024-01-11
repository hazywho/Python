

# Python program to find all subsets of given set. Any
# repeated subset is considered only once in the output
def find_subsets(ind, nums, ds, ans_list):
    ans_list.append(list(ds))
    for i in range(ind, len(nums)):
        if i != ind and nums[i] == nums[i - 1]:
            continue
 
        ds.append(nums[i])
        find_subsets(i + 1, nums, ds, ans_list)
        ds.pop()
 
def all_subsets(arr):
    nums = sorted(arr)
    ans_list = []
    find_subsets(0, nums, [], ans_list)
    return ans_list
 
n,k = 10, 2
with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\subsets.txt") as f:
    for i in f:
        set = list(map(int,i.split(" ")))
news = []
for p in set:
    news.append(p)
subsets = all_subsets(news)
count =0
for subset in subsets:
    for numb in subset:
        count += pow(numb,k,998244353)
print(count)
