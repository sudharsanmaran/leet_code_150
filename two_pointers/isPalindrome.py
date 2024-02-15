def isPalindrome(s: str) -> bool:
    """t O(s + s/2) / s O(s)"""
    alphanum_s = "".join(char for char in s.lower() if char.isalnum())
    l, r = 0, len(alphanum_s) - 1
    while l < r:
        if alphanum_s[l] != alphanum_s[r]:
            return False
        l += 1
        r -= 1

    return True


def isPalindrome_1(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalpha():
            left += 1
        while left < right and not s[right].isalpha():
            right -= 1
        if s[right].lower() != s[left].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(isPalindrome_1(s="A man, a plan, a canal: Panama"))
