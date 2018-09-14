from gerrit_hooks.containers import SupportedHooks, HookFlagDefinitions
from gerrit_hooks.hook import parse_options, build_parser_for, add_custom_approval_category

HOOKS = SupportedHooks()
FLAGS = HookFlagDefinitions()
