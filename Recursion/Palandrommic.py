# given a string calculate the length of longest palandromic calculate the longest palandromic substring.

def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return 0

    # Create a table to store results of subproblems
    dp = [[False] * n for _ in range(n)]
    max_length = 1
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_length = 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                max_length = length

    return max_length
example_string = "abcde"
print("Length of Longest Palindromic Substring is:", longest_palindromic_substring(example_string))

# for every substring check if it is palandromic or not and get the maximum length 