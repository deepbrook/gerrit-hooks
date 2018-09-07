"""Python3 utility to build Gerrit Hook CLI Arg parsers."""
import argparse
import re


# RegEx pattern to parse the flag strings contained in HookType class.
PATTERN = re.compile(r'(?P<flag>--(\w|-)*)\s(?P<description>\<(\w|-|\s)*\>)')


class HookType:

    REF_UPDATE = "--project <project name> --refname <refname> --uploader <uploader> " \
                 "--uploader-username <username> --oldrev <sha1> --newrev <sha1>"

    COMMIT_RECEIVED = "--project <project name> --refname <refname> " \
                      "--uploader <uploader> --uploader-username <username> " \
                      "--oldrev <sha1> --newrev <sha1> --cmdref <refname>"

    SUBMIT = "--project <project name> --branch <branch> --submitter <submitter> " \
             "--patchset <patchset id> --commit <sha1>"

    # --kind may be one of:
    # REWORK, TRIVIAL_REBASE, MERGE_FIRST_PARENT_UPDATE, NO_CODE_CHANGE, NO_CHANGE
    PATCHSET_CREATED = "--change <change id> --kind <change kind> " \
                       "--change-url <change url> --change-owner <change owner> " \
                       "--change-owner-username <username> --project <project name> " \
                       "--branch <branch> --topic <topic> --uploader <uploader> " \
                       "--uploader-username <username> --commit <sha1> " \
                       "--patchset <patchset id>"

    COMMENT_ADDED = "--change <change id> --change-url <change url> " \
                    "--change-owner <change owner> --change-owner-username <username> " \
                    "--project <project name> --branch <branch> --topic <topic> " \
                    "--author <comment author> --author-username <username> " \
                    "--commit <commit> --comment <comment> " \
                    "[--<approval category id> <score> " \
                    "--<approval category id> <score> " \
                    "--<approval category id>-oldValue <score> ...]"

    CHANGE_MERGED = "--change <change id> --change-url <change url> " \
                    "--change-owner <change owner> --change-owner-username <username> " \
                    "--project <project name> --branch <branch> --topic <topic> " \
                    "--submitter <submitter> --submitter-username <username> " \
                    "--commit <sha1> --newrev <sha1>"

    CHANGE_ABANDONED = "--change <change id> --change-url <change url> " \
                       "--change-owner <change owner> " \
                       "--change-owner-username <username> " \
                       "--project <project name> --branch <branch> " \
                       "--topic <topic> --abandoner <abandoner> " \
                       "--abandoner-username <username> --commit <sha1> " \
                       "--reason <reason>"

    CHANGE_RESTORED = "--change <change id> --change-url <change url> " \
                      "--change-owner <change owner> " \
                      "--change-owner-username <username> --project <project name> " \
                      "--branch <branch> --topic <topic> --restorer <restorer> " \
                      "--restorer-username <username> --commit <sha1> " \
                      "--reason <reason>"

    REF_UPDATED = "--oldrev <old rev> --newrev <new rev> --refname <ref name> " \
                  "--project <project name> --submitter <submitter> " \
                  "--submitter-username <username>"

    PROJECT_CREATED = "--project <project name> --head <head name>"

    REVIEWER_ADDED = "--change <change id> --change-url <change url> " \
                     "--change-owner <change owner> " \
                     "--change-owner-username <username> " \
                     "--project <project name> --branch <branch> " \
                     "--reviewer <reviewer> --reviewer-username <username>"

    REVIEWER_DELETED = "--change <change id> --change-url <change url> " \
                       "--change-owner <change owner> " \
                       "--change-owner-username <username> " \
                       "--project <project name> --branch <branch> " \
                       "--reviewer <reviewer> [--<approval category id> <score> " \
                       "--<approval category id> <score> ...]"

    TOPIC_CHANGED = "--change <change id> --change-owner <change owner> " \
                    "--change-owner-username <username> --project <project name> " \
                    "--branch <branch> --changer <changer> --changer-username <username> " \
                    "--old-topic <old topic> --new-topic <new topic>"

    # --hashtag, --added and --removed may be passed multiple times
    HASHTAGS_CHANGED = "--change <change id>  --change-owner <change owner> " \
                       "--change-owner-username <username> --project <project name> " \
                       "--branch <branch> --editor <editor> " \
                       "--editor-username <username> --added <hashtag> " \
                       "--removed <hashtag> --hashtag <hashtag>"

    CLA_SIGNED = "--submitter <submitter> --user-id <user_id> --cla-id <cla_id>"

    __all__ = [
        REF_UPDATE, REF_UPDATED, PATCHSET_CREATED, CLA_SIGNED, TOPIC_CHANGED,
        PROJECT_CREATED, REVIEWER_ADDED, REVIEWER_DELETED, HASHTAGS_CHANGED,
        CHANGE_ABANDONED, CHANGE_MERGED, CHANGE_RESTORED, COMMENT_ADDED,
        COMMIT_RECEIVED, SUBMIT,
    ]


def flag_string_to_dict(flag_string):
    """Extract flag - description pairs from the given string.

    :rtype: dict
    """
    return {match.flag: match.description
            for match in PATTERN.finditer(flag_string)}


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
    cli_flags = flag_string_to_dict(hook_type)
    return _generate_parser(**cli_flags)


def parse_options(hook_type):
    """Build a parser and parse the CLI options for the given hook type.

    :param str hook_type: The type of hook to build and parse options for.
    :rtype: Type[argparse.NameSpace]
    """
    if hook_type not in HookType.__all__:
        raise ValueError("Unknown Hook type: {}".format(hook_type))
    return build_parser_for(hook_type).parse_args()

