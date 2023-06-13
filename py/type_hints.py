from typing import List, Dict

# 型ヒント
# https://docs.python.org/ja/3/library/typing.html
sample_list: List[int] = [1, 2, 3, 4]
sample_dict: Dict[str, int] = {'key1': 1, 'key2': 2}

price: int = 100
tax: float = 1.1


def calc_price_including_tax(price: int, tax: float) -> int:
    return int(price * tax)


if __name__ == '__main__':
    print(f'{calc_price_including_tax(price, tax)}円')
