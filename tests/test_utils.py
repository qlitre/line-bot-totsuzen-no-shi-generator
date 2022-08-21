from utils import utils


def test_get_east_asian_width_count():
    text = 'WRYYY'
    assert utils.get_east_asian_width_count(text) == 5
    text = '鉛筆なめなめ'
    assert utils.get_east_asian_width_count(text) == 12
    text = 'Excelで転記'
    assert utils.get_east_asian_width_count(text) == 11


def test_get_bottom_line():
    # pattern WRYYY
    top_count = 5
    assert utils.get_bottom_line(top_count) == '￣Y^Y^Y^Y^￣'
    # pattern 鉛筆なめなめ
    top_count = 8
    assert utils.get_bottom_line(top_count) == '￣Y^Y^Y^Y^Y^Y^￣'


def test_decorate_message():
    text = 'WRYYY'
    print(utils.decorate_message(text))
    assert utils.decorate_message(text)
    text = '鉛筆なめなめ'
    print(utils.decorate_message(text))
    assert utils.decorate_message(text)
    text = 'Excelで転記'
    print(utils.decorate_message(text))
    assert utils.decorate_message(text)
