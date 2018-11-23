"""Utility methods for creating argparse.ArgumentParser Gerrit Hooks."""
import argparse
import pathlib

from __main__ import __file__

from gerrit_hooks.containers import HOOKS, FLAGS
from gerrit_hooks.utils import normalize_hook_name


def _generate_parser(**cli_kwargs):
    """Set up an argument parser with the given expected options.

    :param Any cli_kwargs:
        Kwargs containing configuration details for a CLI flag.
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser()
    for flag, details in cli_kwargs.items():
        description, options = details
        parser.add_argument(flag, help=description, required=False, **options)
    return parser


def build_parser_for(hook_type):
    """Build an argument parser for the given hook string.

    `hook_type` is normalized to all upper-case letters, and any "-" characters
    are replaced with under scores ("_"). Most of the time the value of
    `hook_type` is expected to be the file name, which is also the name of the
    hook. Since Container classes expect the attribute name as keys, this
    normalization is necessary in order to avoid KeyErrors.

    :param str hook_type:
        The hook type string to generate an argument parser from.
    :rtype: argparse.ArgumentParser
    """
    hook_type = normalize_hook_name(hook_type)
    cli_flags = FLAGS[hook_type]
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
    :rtype: argparse.NameSpace
    """
    hook_type = pathlib.Path(hook_type).stem
    normalized_hook_type = normalize_hook_name(hook_type)
    if hook_type not in HOOKS:
        raise ValueError("Unknown Hook type: {}".format(normalized_hook_type))
    return build_parser_for(hook_type).parse_args()
