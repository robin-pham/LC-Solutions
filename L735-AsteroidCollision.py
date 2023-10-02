# 735 - Asteroid Collision


# queue of asteroids moving left (-ve) or right(+ve)
# if two meet, smaller explodes, if same size, they both explode
# use a stack to access the last item we've parsed through


def asteroid_collision(asteroids):
    stack = []
    for asteroid in asteroids:
        if not stack or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0):
            stack.append(asteroid)
        else:
            remaining = asteroid
            while remaining:
                last = stack.pop()
                if abs(last) == abs(remaining):
                    remaining = None
                else:
                    remaining = last if abs(last) > abs(asteroid) else asteroid
                    if (
                        not stack
                        or (stack[-1] > 0 and remaining > 0)
                        or (stack[-1] < 0)
                    ):
                        stack.append(remaining)
                        remaining = None
    return stack


asteroids = [-2, -1, 1, 2]
print(asteroid_collision(asteroids))
