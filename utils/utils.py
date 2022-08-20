import unicodedata
import math


def get_east_asian_width_count(text: str) -> int:
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count


def decorate_message(msg: str) -> str:
    """
    messageを受け取り以下のようにデコって返す
    ＿人人人人人人＿
    ＞  突然の死　＜
    ￣Y^Y^Y^Y^Y￣
    """
    length = get_east_asian_width_count(msg)
    cnt = math.ceil(length / 2) + 2
    top = f'＿{"人" * cnt}＿'
    bottom = f'￣{"Y^" * (cnt - 1)}'[:-1]
    bottom += '￣'
    reply = f'{top}\n＞　{msg}　＜\n{bottom}'
    return reply
