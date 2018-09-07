# Gerrit Hooks Interfaces

This library provides argumentparsers for gerrit's hooks-plugin's hook files.

It allows developers to get started with gerrit hooks faster, by 
getting the parsing of command-line arguments for the various hook types
 out of the way.

All hooks are supported.

# Installation

```
pip install gerrit-hooks
```

# Usage

Writing hooks using gerrit-hooks' argparsers is easy:

```python
> gerrit/hooks/comment-added

#!/usr/bin/env/python3
import gerrit_hooks

parser = gerrit_hooks.build_parser_for(gerrit_hooks.COMMENT_ADDED)

options = parser.parse()

print("Change ID: {}".format(options.change))
...

```


# Resources

## Gerrit Hooks Plugin Repository:

https://gerrit-review.googlesource.com/admin/repos/plugins%2Fhooks
