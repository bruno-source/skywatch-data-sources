import click
from tabulate import tabulate

from skywatch_data_sources.sources import get_data_sources


@click.command('list_data_sources')
def list_data_sources():
    """
    Parses www.skywatch.com and returns a list of its available data sources
    in a pretty-printed tabular data.
    """
    sources = get_data_sources()

    if sources:
        table = tabulate(sources, headers='keys', tablefmt='fancy_grid')
        click.echo(click.style(table, fg='green'))
    else:
        click.echo(click.style('Could not retrieve data sources', fg='red'))
