# Gerrit Hooks Argument Parsers

This library provides pre-built `argparse.ArgumentParser` instances, which
return `argpase.NameSpace` object for gerrit's hooks (linked in the [Resources](#resources) section below).


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

Custom approval categories are supported as well - these must be added
before calling `gerrit_hooks.parse_options()`:

```python
> gerrit/hooks/comment-added

#!/usr/bin/env/python3
import gerrit_hooks

# Let's assume you have a approval category with label 'level-of-amazingness
# We need to add this to the Hook Flag Definitions class
gerrit_hooks.add_custom_approval_rating('level-of-amazingness')

options = gerrit_hooks.parse_options()

# The approval category can be accessed by the following attributes:
print("Level of Amazingness is: {}".format(options.level_of_amazingness))
print("Level of Amazingness was: {}".format(options.level_of_amazingness_oldValue))

...

```

# Resources

[Gerrit-Hooks Plugin](https://gerrit-review.googlesource.com/admin/repos/plugins%2Fhooks)
