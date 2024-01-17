"""This is 1st task for OTUS"""
def calculate_average(nums1):
    """Function for calculating average"""

    total = sum(nums1)
    count = len(nums1)
    return total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
