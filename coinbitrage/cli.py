# -*- coding: utf-8 -*-
import click
from coinbitrage import exchange_diff, format_float_decimals
from terminaltables.other_tables import SingleTable


@click.group()
def main():
    pass


@main.command()
@click.argument('exchange1')
@click.argument('exchange2')
@click.option('--reverse', help='reverse ordering', is_flag=True)
@click.option('--sort-by', help='which column to sort by [diff, diff_perc]', default='diff_perc', show_default=True)
def diff(exchange1, exchange2, reverse, sort_by):
    """show difference between two exchanges"""
    diff = exchange_diff(exchange1, exchange2, sort_by=sort_by, sort_reverse=not reverse)
    headers = ['currency'] + list(diff[list(diff.keys())[0]].keys())
    rows = [[k] + list(v.values()) for k, v in diff.items()]
    # format all float to reduce decimal places
    rows = [[format_float_decimals(el) if isinstance(el, float) else el for el in r]
            for r in rows]
    s = SingleTable([headers] + rows)
    click.echo(s.table)


if __name__ == "__main__":
    main()
