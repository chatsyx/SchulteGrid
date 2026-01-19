import random

def generate_grid(n):
    """生成n×n舒尔特方格数字，1~n²随机无重复"""
    nums = list(range(1, n*n + 1))
    random.shuffle(nums)
    grid = [nums[i*n : (i+1)*n] for i in range(n)]
    return grid