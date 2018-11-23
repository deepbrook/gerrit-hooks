"""Container class for the gerrit-hooks library.

Supplies containers which store supported hooks, as well as flag definitions.
"""
from gerrit_hooks.actions import AppendHashtag
from gerrit_hooks.containers.base import Container


class FlagOptions(Container):
    """Container class for special flag options."""
    #: Custom Config for the hashtag-* hooks. It may be passed multiple times,
    #  so the action needs to be an append instead of a store.
    HASHTAG = {'nargs': 1, 'action': AppendHashtag}
    ADDED = {'nargs': 1, 'action': AppendHashtag}
    REMOVED = {'nargs': 1, 'action': AppendHashtag}

    #: patchset-created's --kind only has a select range of allowed arguments.
    KIND = {
        "nargs": 1,
        "choices": [
            "REWORK",
            "TRIVIAL_REBASE",
            "MERGE_FIRST_PARENT_UPDATE",
            "NO_CODE_CHANGE",
            "NO_CHANGE"
        ]
    }

    # gerrit may pass the --topic flag without an argument following it. Support
    # this, by defaulting to None if that's the case. Note that because --topic
    # is optional, we need to specify the value we'd like to be used instead of
    # the missing argument as the `const` value.
    # See the docs for more information on why:
    #   https://docs.python.org/3/library/argparse.html#nargs
    TOPIC = {"nargs": "?", "const": "", "default": ""}


FLAG_OPTIONS = FlagOptions()