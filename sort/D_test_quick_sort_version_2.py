from sort.sort_helper import generate_random_array
from sort.C_merge_sort_1 import merge_sort
from sort.D_quick_sort_2 import quick_sort
from sort.sort_helper import check_sorted
import time

# 最小值是 10，最大值是 12，都可以取到
# 取了 10000 个元素，用快排 2 和归并排序测试一下
nums = generate_random_array(10, 12, 10000)
print(nums)

nums_for_merge_sort = nums[:]
nums_for_quick_sort_2 = nums[:]

begin = time.time()
merge_sort(nums_for_merge_sort)
print('归并排序第 1 版耗时：', time.time() - begin)

begin = time.time()
quick_sort(nums_for_quick_sort_2)
print('快速排序第 2 版耗时：', time.time() - begin)

check_sorted(nums, nums_for_merge_sort)
check_sorted(nums, nums_for_quick_sort_2)
