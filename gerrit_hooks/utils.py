"""Utility methods for creating parsers and namespaces for CLI flags."""
from gerrit_hooks.containers import FLAGS


def add_custom_approval_category(label):
    """Add a custom approval category to the Hook flag definitions.

    :param str label: Label of the approval category.
    """
    FLAGS.add_approval_category(label)


def normalize_hook_name(hook):
    """Normalize the hook name.

    When the hook name is initially passed, it's assumed that it's the file
    name in most cases. This is usually a lower-cased string, containing several
    words connected by dashes ("-"). The library looks up configuration data
    using an upper-cased version of the hook names, with underscores replacing
    the dashes ("_" instead of "-"). This method takes care of the conversion.

    Example::

        >>>normalize_hook_name("patchset-created")
        "PATCHSET_CREATED"

    """
    hook = hook.upper()
    hook = hook.replace("-", "_")
    return hook