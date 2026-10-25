class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical_set: list[set[str]] = [set() for _ in range(9)]
        group_set: list[set[str]] = [set() for _ in range(9)]

        for i in range(9):
            horizontal_set = set()

            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                group = i // 3 * 3 + j // 3

                if (
                    value in horizontal_set
                    or value in vertical_set[j]
                    or value in group_set[group]
                ):
                    return False

                horizontal_set.add(value)
                vertical_set[j].add(value)
                group_set[group].add(value)

        return True

