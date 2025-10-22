import function

def count_word(s, mozi):
    answer = 0
    for now in s:
        if now==mozi:
            answer = function.add(answer,1)
    return answer