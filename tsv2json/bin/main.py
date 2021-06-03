import sys

import click

from tsv2json import version_info
from tsv2json.core import TSV


@click.command(name='tsv2json',
               no_args_is_help=True,
               help=click.style(version_info['desc'], bold=True, fg='cyan')
               )
@click.argument('infile')
@click.option('-s', '--sep', help='the seperator of infile', default='\t', show_default=True)
@click.option('-o', '--outfile', help='the output file[stdout]')
@click.option('-l', '--limit', help='lines limit for infile', type=int)
@click.option('-H', '--header', help='assume infile has header', type=click.BOOL, default=True, show_default=True)
@click.option('-c', '--comment', help='ignore lines which startswith comment, if comment is supplied')
@click.option('-i', '--indent', help='the indent of output json', type=int)
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
def cli(**kwargs):


    # when tab('\t') input, we got '\\t' actually, need convert to '\t'
    kwargs['sep'] = eval('"{}"'.format(kwargs['sep']))

    tsv = TSV(kwargs['infile'], **kwargs)

    res = tsv.to_json(kwargs['outfile'], indent=kwargs['indent'])
    if res:
        print(res)


def main():
    cli()


if __name__ == '__main__':
    main()
