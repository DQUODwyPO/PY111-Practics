def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    cnt = 0
    for i in range(len(brackets_row)):
        if brackets_row[i] == "(":
            cnt += 1
        elif brackets_row[i] == ")":
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        return True
    return False
