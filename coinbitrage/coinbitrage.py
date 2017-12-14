# -*- coding: utf-8 -*-
from collections import OrderedDict, namedtuple
from typing import List, Union

import requests
import parsel


def download_coin(coin):
    pass
    # for row in resp.css('#markets-table>tbody>tr'):
    #     xp_first = lambda xp: row.xpath('td[1]/text()').extract_first()
    #     item = {
    #         'rank': xp_first('td[1]/text()'),
    #         'exchange': xp_first('td[2]//text()'),
    #         'pair': xp_first('td[3]//text()'),
    #     }


def download_exchange(exchange: str) -> dict:
    """
    Download exchange data
    :param exchange: exchange name
    :return: dict of currency: usd_price
    """
    url = f'https://coinmarketcap.com/exchanges/{exchange}/'
    resp = requests.get(url)
    sel = parsel.Selector(text=resp.text, base_url=resp.url)
    results = {}
    for row in sel.css('.table-condensed>tr')[1:]:
        name = row.css('.market-name::text').extract_first()
        usd = float(row.css('.price::attr(data-usd)').extract_first())
        if name and usd:
            results[name] = usd
    return results


Price = namedtuple('Price', ['exchange', 'diff', 'diff_perc'])


def price_diff(data1: dict, data2: dict, sort_by: str='diff_perc', sort_reverse=True) -> List[Price]:
    """
    :param data1: exchange data1
    :param data2: exchange data2
    :param sort_by: sort results by key: exchange, diff, diff_perc
    :param sort_reverse: whether sort in descending order
    :return: sorted list of Price objects
    """
    results = []
    for k in data1:
        if k not in data2:
            continue
        diff = abs(data1[k] - data2[k])
        diff_perc = 100 - (data2[k] / data1[k] * 100)
        results.append(Price(k, diff, diff_perc))
    results = sorted(results, key=lambda price: getattr(price, sort_by), reverse=sort_reverse)
    return results


def exchange_diff(exchange1: str, exchange2: str, sort_by='diff_perc', sort_reverse=True) -> dict:
    """

    :param data1: exchange data1
    :param data2: exchange data2
    :param sort_by: sort results by key: exchange, diff, diff_perc
    :param sort_reverse: whether sort in descending order
    :return: dictionary containing currency data
    """
    data1 = download_exchange(exchange1)
    data2 = download_exchange(exchange2)
    price_d = price_diff(data1, data2, sort_by=sort_by, sort_reverse=sort_reverse)
    results = OrderedDict()
    for k, diff, diff_perc in price_d:
        results[k] = OrderedDict([
            (exchange1, data1[k]),
            (exchange2, data2[k]),
            ("diff", diff),
            ("diff_perc", diff_perc),
        ])
    return results


def format_float_decimals(num: Union[int, float]) -> str:
    if num < 1:
        return f'{num:.5f}'
    if num < 10:
        return f'{num:.3f}'
    if num < 100:
        return f'{num:.2f}'
    if num < 1000:
        return f'{num:.1f}'
    return f'{num:.0f}'


def pretty_print_diff(diff):
    exchange1, exchange2 = [k for k in diff[list(diff.keys())[0]] if k not in ['diff', 'diff_perc']]
    header = f'{"currency":<20}{exchange1:<13}{exchange2:<13}{"diff":>13}{"diff %":>13}'
    print(header)
    print(len(header) * '-')
    for k, v in diff.items():
        v[exchange1] = format_float_decimals(v[exchange1])
        v[exchange2] = format_float_decimals(v[exchange2])
        v['diff'] = format_float_decimals(v['diff'])
        v['diff_perc'] = format_float_decimals(v['diff_perc'])
        print(f'{k:<20}{v[exchange1]:<13}{v[exchange2]:<13}{v["diff"]:>13}{v["diff_perc"]:>13}')
