# Gerrit Hooks Argument Parsers

This library provides pre-built `argparse.ArgumentParser` instances 
for gerrit's hooks (linked in the [Resources](#resources) section below).


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

options = gerrit_hooks.parse_options()

print("Change ID: {}".format(options.change))
...

```


# Resources

[Gerrit-Hooks Plugin](https://gerrit-review.googlesource.com/admin/repos/plugins%2Fhooks)
