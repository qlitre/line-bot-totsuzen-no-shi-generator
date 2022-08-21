import unicodedata
import math


def get_east_asian_width_count(text: str) -> int:
    """
    textを受け取りeast asian widthを返す。
    つまり、半角が1,全角が2
    """
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count


def get_bottom_line(top_count: int) -> str:
    """
    文字の上側の1set"人"に対して下側の1set"Y^"が微妙に長さが違うので、
    微調整を行う。
    人人
    Y^Y
    ここで大体あうので、
    "人":5
    "Y":4
    "^":2
    という比率と仮定。
    """
    top_length = top_count * 5
    # Yと^を足した6で割って切り下げた数を繰り返し数とする
    bottom_count = math.floor(top_length / 6)
    bottom_string = "Y^" * bottom_count

    return f'￣{bottom_string}￣'


def decorate_message(msg: str) -> str:
    """
    messageを受け取り以下のようにデコって返す
    ＿人人人人人人＿
    ＞  突然の死　＜
    ￣Y^Y^Y^Y^Y￣
    """
    length = get_east_asian_width_count(msg)
    top_count = math.ceil(length / 2) + 2
    top = f'＿{"人" * top_count}＿'
    bottom = get_bottom_line(top_count)
    reply = f'{top}\n＞　{msg}　＜\n{bottom}'
    return reply
