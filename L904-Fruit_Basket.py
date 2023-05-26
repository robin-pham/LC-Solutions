L904 - Fruit_Basket.py


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruit = 1
        fruit_basket = {fruits[0]}
        search_start = search_position = current_fruit = 0

        while search_position < len(fruits):
            while len(fruit_basket) < 3:
                current_fruit = (
                    search_position
                    if fruits[search_position] != fruits[search_position - 1]
                    else current_fruit
                )
                max_fruit = (
                    search_position - search_start + 1
                    if search_position - search_start + 1 > max_fruit
                    else max_fruit
                )

                search_position += 1
                if search_position == len(fruits):
                    return max_fruit
                fruit_basket.add(fruits[search_position])
            search_start = current_fruit
            fruit_basket = {fruits[search_start], fruits[search_position]}
        return max_fruit


# time O(N), space O(1)
