L6 - Zigzag_Conversion


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row = [[] for _ in range(numRows)]
        unstacked = []
        down = True
        for ch in s:
            row[-1].append(ch)
            unstacked.append(row.pop())
            if not row:
                row, unstacked = unstacked, row
                unstacked.append(row.pop())
                down = not down
        while row:
            unstacked.append(row.pop())
        print(unstacked)
        zigzag = ["".join(line) for line in unstacked]
        return "".join(zigzag[::-1]) if not down else "".join(zigzag)
