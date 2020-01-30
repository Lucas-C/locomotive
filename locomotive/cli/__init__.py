"""
Locomotive CLI.
"""

import logging
from typing import Any

import click

from ..stores import Stations
from .commands.search import search


@click.group()
@click.option("--debug", is_flag=True)
@click.option(
    "--stations-file",
    metavar="PATH",
    default=Stations.default_path(),
    show_default=True,
)
@click.pass_context
def cli(ctx: click.Context, **args: Any) -> None:
    """
    🚆 Search SNCF journeys from your terminal.

    \b
    Examples:
    sncf-cli search Brest Paris
    """
    if args["debug"]:
        logging.basicConfig(level=logging.DEBUG)

    ctx.ensure_object(dict)
    ctx.obj["stations"] = Stations(path=args["stations_file"])


cli.add_command(search)
