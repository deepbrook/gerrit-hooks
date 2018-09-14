"""Python3 utility to build Gerrit Hook CLI Arg parsers."""
import argparse
import pathlib
from __main__ import __file__

from gerrit_hooks.containers import SupportedHooks, HookFlagDefinitions


def add_custom_approval_category(label):
    """Add a custom approval category to the Hook flag definitions.

    :param str label: Label of the approval category.
    """
    HookFlagDefinitions.add_approval_category(label)


def _generate_parser(**cli_kwargs):
    """Set up an argument parser with the given expected flags as kwargs.

    :param Any kwargs: Flag=Description kwarg pairs.
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser()
    for flag, description, options in cli_kwargs.items():
        parser.add_argument(flag, description=description, required=False, **options)
    return parser


def build_parser_for(hook_type):
    """Build an argument parser for the given hook string.

    :param str hook_type: The hook type string to generate an argument parser from.
    :rtype: argparse.ArgumentParser
    """
    cli_flags = HookFlagDefinitions()[hook_type]
    return _generate_parser(**cli_flags)


def parse_options(hook_type=__file__):
    """Build a parser and parse the CLI options for the given hook type.

    We support passing `__file__`, which may or may not be an absolute path
    (depending on the platform) - if it is, we use the pathlib module to
    exctract the hook's name.
    To do this, we convert ``hook_type`` to a pathlib.Path object and get its
    pathlib.Path.stem property - which is the last part of the path, sans
    extension, if any.

    :param str hook_type: The type of hook to build and parse options for.
    :raises ValueError: If hook_type is not found in the SupportedHooks container.
    :rtype: Type[argparse.NameSpace]
    """
    hook_type = pathlib.Path(hook_type).stem

    if hook_type not in SupportedHooks():
        raise ValueError("Unknown Hook type: {}".format(hook_type))
    return build_parser_for(hook_type).parse_args()

