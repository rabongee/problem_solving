def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                prime = nums[i] + nums[j] + nums[k]
                TF = True
                for num in range(2, prime):
                    if prime % num == 0:
                        TF = False
                if TF == True:
                    answer += 1
    return answer