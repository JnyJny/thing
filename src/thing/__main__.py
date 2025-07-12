"""thing CLI implementation.

Thing for humans, presumably like you!
"""

import sys

import typer
from loguru import logger

from .self_subcommand import cli as self_cli
from .settings import Settings

cli = typer.Typer()

cli.add_typer(
    self_cli,
    name="self",
    help="Manage the thing command.",
)


@cli.callback(invoke_without_command=True, no_args_is_help=True)
def global_callback(
    ctx: typer.Context,
    debug: bool = typer.Option(
        False,
        "--debug",
        "-D",
        help="Enable debugging output.",
    ),
) -> None:
    """Thing for humans, presumably like you!"""
    ctx.obj = Settings()
    debug = debug or ctx.obj.debug
    (logger.enable if debug else logger.disable)("thing")
    logger.add("thing.log")
    logger.info(f"{debug=}")


if __name__ == "__main__":
    sys.exit(cli())
