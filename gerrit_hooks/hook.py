"""Python3 utility to build Gerrit Hook CLI Arg parsers."""
import argparse

from gerrit_hooks import HOOKS, FLAGS


def _generate_parser(**cli_kwargs):
    """Set up an argument parser with the given expected flags as kwargs.

    :param Any kwargs: Flag=Description kwarg pairs.
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser()
    for flag, description in cli_kwargs.items():
        parser.add_argument(flag, description=description)
    return parser


def build_parser_for(hook_type):
    """Build an argument parser for the given hook string.

    :param str hook_type: The hook type string to generate an argument parser from.
    :rtype: argparse.ArgumentParser
    """
    cli_flags = FLAGS[hook_type]
    return _generate_parser(**cli_flags)


def parse_options(hook_type):
    """Build a parser and parse the CLI options for the given hook type.

    :param str hook_type: The type of hook to build and parse options for.
    :rtype: Type[argparse.NameSpace]
    """
    if hook_type not in HOOKS:
        raise ValueError("Unknown Hook type: {}".format(hook_type))
    return build_parser_for(hook_type).parse_args()

