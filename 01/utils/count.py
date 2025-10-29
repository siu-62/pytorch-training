import function

def count_word(s, mozi):
    assert isinstance(s,str), "文字列からじゃないと中身数えらんないよ"
    assert isinstance(mozi,str) and mozi.length == 1, "文字列からじゃないと中身数えらんないよ"
    assert mozi
    answer = 0
    for now in s:
        if now==mozi:
            answer = function.add(answer,1)
    return answer