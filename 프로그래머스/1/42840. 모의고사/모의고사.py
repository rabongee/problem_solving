def solution(answers):
    answer = []
    math_giveup1=[1,2,3,4,5]
    math_giveup2=[2,1,2,3,2,4,2,5]
    math_giveup3=[3,3,1,1,2,2,4,4,5,5]
    cnt_1=0
    cnt_2=0
    cnt_3=0
    for i, ans in enumerate(answers):
        if ans == math_giveup1[i%len(math_giveup1)]:
            cnt_1+=1
        if ans ==math_giveup2[i%len(math_giveup2)]:
            cnt_2+=1
        if ans == math_giveup3[i%len(math_giveup3)]:
            cnt_3+=1
    answer_check=[cnt_1,cnt_2,cnt_3]
    for i in range(len(answer_check)):
        if answer_check[i]==max(answer_check):
            answer.append(i+1)
    return answer
