def subsequence(input,output):
    if len(input)==0:
        print(output,end=" ")
        return 

    subsequence(input[1:],output+input[0])
    subsequence(input[1:], output)


output = ""
input = "abcd"

subsequence(input, output)