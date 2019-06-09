"""
Locomotive CLI.
"""

import click

from ..passengers import Passengers

from .config import config
from .passengers import passengers
from .search import search


@click.group()
@click.option("--debug", is_flag=True)
@click.option(
    "--passengers-file",
    metavar="PATH",
    default=Passengers.default_path(),
    show_default=True,
)
)
@click.pass_context
def cli(ctx, **args):
    """
    🚆 Search SNCF journeys from your terminal.

    \b
    Examples:
    sncf-cli search Brest Paris
    """
    ctx.ensure_object(dict)
    # Load global objects
    ctx.obj["passengers"] = Passengers(path=args["passengers_file"])


cli.add_command(passengers)
cli.add_command(search)
