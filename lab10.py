
def eval_rpn(tokens: list[str]) -> int:
    # Outline: Push numbers, pop operands and calculate.
    stack = []

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack.pop()


def decode_string(s: str) -> str:
    # Outline: Save strings and repeat counts on a stack.
    stack = []
    current = ""
    number = 0

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == "[":
            stack.append((current, number))
            current = ""
            number = 0
        elif char == "]":
            previous, repeat = stack.pop()
            current = previous + current * repeat
        else:
            current += char

    return current


def daily_temperatures(temps: list[int]) -> list[int]:
    # Outline: Track waiting days using a stack of indices.
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous = stack.pop()
            result[previous] = i - previous

        stack.append(i)

    return result


def num_islands(grid: list[str]) -> int:
    # Outline: Explore connected land and mark visited cells.
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                stack = [(r, c)]
                visited.add((r, c))

                while stack:
                    x, y = stack.pop()

                    for dx, dy in [(1, 0), (-1, 0),
                                   (0, 1), (0, -1)]:
                        nx = x + dx
                        ny = y + dy

                        if (0 <= nx < rows
                                and 0 <= ny < cols
                                and grid[nx][ny] == "1"
                                and (nx, ny) not in visited):
                            visited.add((nx, ny))
                            stack.append((nx, ny))

    return islands
