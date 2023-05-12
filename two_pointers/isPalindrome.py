def isPalindrome(s: str) -> bool:
    """t O(s + s/2) / s O(s)"""
    alphanum_s = ''.join(char for char in s.lower() if char.isalnum())
    l, r = 0, len(alphanum_s) - 1
    while l < r:
        if alphanum_s[l] != alphanum_s[r]:
            return False
        l += 1
        r -= 1

    return True


if __name__ == '__main__':
    print(isPalindrome(s="A man, a plan, a canal: Panama"))
