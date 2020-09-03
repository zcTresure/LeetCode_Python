def majorityElement(self, nums: list) -> list:
    ans = []
    n = len(nums)

    def judge(major: int, count: int, n: int) -> None:
        counts = 0
        if count >= 0:
            for num in nums:
                if major == num:
                    counts += 1
        if counts > (n // 3):
            ans.append(major)

    major1 = major2 = -1
    count1 = count2 = 0
    for num in nums:
        if count1 == 0 and major2 != num:
            major1 = num
            count1 +=1
        elif count2 == 0 and major1 != num:
            major2 = num
            count2 +=1
        else:
            if major1 == num:
                count1 += 1
            elif major2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
    judge(major1, count1, n)
    judge(major2, count2, n)
    return ans


nums = [3, 3, 2]
print(majorityElement(1, nums))
