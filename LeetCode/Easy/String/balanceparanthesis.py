def balanced(exp):
    stack = []

    for ch in exp:
        if ch in ["(","[","{"]:
            stack.append(ch)
        else:

            if not stack:
                return False
            curr_ch = stack.pop()
            if curr_ch == "(":
                if ch != ")":
                    return False
            if curr_ch == "{":
                if ch != "}":
                    return False
            if curr_ch == "[":
                if ch != "]":
                    return False

        if stack:
            return False
        return True

if __name__=="__main__":
    exp = "{()}[]"
    if balanced(exp):
        print("Balanced")
    else:
        print("Not Balanced")                                                