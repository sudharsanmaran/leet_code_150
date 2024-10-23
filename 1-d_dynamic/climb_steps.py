def climbStairs(n: int) -> int:
    combination = 0

    def backtrack(steps):
        nonlocal combination

        if steps == n:
            combination += 1
            return
        elif steps > n:
            return

        backtrack(steps + 1)
        backtrack(steps + 2)

    backtrack(0)
    return combination


# through dp
def climb_stairs(n: int) -> int:
    one, two = 1, 2
    for _ in range(3, n):
        temp = two
        two = one + two
        one = temp
    return one + two


print(climb_stairs(5))
