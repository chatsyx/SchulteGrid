import random

def generate_grid(n):
    """生成n×n数字网格（原有功能，保留），1~n²随机无重复"""
    nums = list(range(1, n*n + 1))
    random.shuffle(nums)
    grid = [nums[i*n : (i+1)*n] for i in range(n)]
    return grid

def generate_letter_grid(n):
    """v1.1新增：生成n×n字母网格，a~对应字母随机无重复"""
    # 生成对应数量字母（a=97，按n²数量生成，支持3~7阶）
    letters = [chr(97 + i) for i in range(n*n)]
    random.shuffle(letters)  # 随机打乱
    grid = [letters[i*n : (i+1)*n] for i in range(n)]
    return grid