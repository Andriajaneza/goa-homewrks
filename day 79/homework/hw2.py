def gamocdebi(score):
    if score > 90 and score < 100:
        return "შესანიშნავი!"
    if score > 75 and score < 89:
        return "კარგი!"
    if score > 50 and score < 74:
        return "საშუალო!"
    if score > 30 and score < 49:
        return "სუსტია!"
    if score > 0 and score < 29:
        return "ჩავარდნა!"
