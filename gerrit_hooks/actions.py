import argparse


class AppendHashtag(argparse._AppendAction):
    """Customized Action class for argparse._AppendAction.

    The original implementation appends the values as a list of strings. Since
    hashtags are only ever passed as single values via CLI, we essentially end
    up with a list of list of single strings.

    Iterating over such a list will require a lambda or similar, in order to
    access the 0 index of each list.

    This class removes this requirement by storing the hashtag as string, rather
    than a list of a single string.
    """
    def __call__(self, parser, namespace, values, option_string=None):
        """Append the tag as a string, instead of a list of str.

        Hashtags are always passed as single values, and hence do not need to
        be passed as a list, which makes iterating over them difficult.
        """
        items = getattr(namespace, self.dest, None)
        items = argparse._copy_items(items)
        for tag in self.const:
            items.append(tag)
        setattr(namespace, self.dest, items)
