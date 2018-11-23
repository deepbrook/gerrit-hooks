"""Container class for the gerrit-hooks library.

Supplies containers which store supported hooks, as well as flag definitions.
"""
import re

from gerrit_hooks.containers.base import Container
from gerrit_hooks.containers.flag_configs import FLAG_OPTIONS


class HookFlagDefinitions(Container):
    """Container class for each supported hook's supported CLI flags.

    The parameters were taken from the :ref:`Hook Documenation`_.

    .._Hook Documentation:https://gerrit.googlesource.com/plugins/hooks/+/refs/heads/stable-2.15/src/main/resources/Documentation/hooks.md#supported-hooks
    """

    #: RegEx pattern to parse the flag strings contained in HookType class.
    FLAG_PATTERN = re.compile(r'(?P<flag>--(\w|-)*)\s(?P<description>\<(\w|-|\s)*\>)')

    REF_UPDATE = [
        "--project <project name>",
        "--refname <refname>",
        "--uploader <uploader>",
        "--uploader-username <username>",
        "--oldrev <sha1>",
        "--newrev <sha1>",
    ]

    COMMIT_RECEIVED = [
        "--project <project name>",
        "--refname <refname>",
        "--uploader <uploader>",
        "--uploader-username <username>",
        "--oldrev <sha1>",
        "--newrev <sha1>",
        "--cmdref <refname>",
    ]

    SUBMIT = [
        "--project <project name>",
        "--branch <branch>",
        "--submitter <submitter>",
        "--patchset <patchset id>",
        "--commit <sha1>",
    ]

    PATCHSET_CREATED = [
        "--change <change id>",
        "--kind <change kind>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--topic <topic>",
        "--uploader <uploader>",
        "--uploader-username <username>",
        "--commit <sha1>",
        "--patchset <patchset id>",
    ]

    COMMENT_ADDED = [
        "--change <change id>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--topic <topic>",
        "--author <comment author>",
        "--author-username <username>",
        "--commit <commit>",
        "--comment <comment>",
        "--Code-Review <score>",
        "--Verified <score>",
        "--Code-Review-oldValue <score>",
        "--Verified-oldValue <score>",
    ]

    CHANGE_MERGED = [
        "--change <change id>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--topic <topic>",
        "--submitter <submitter>",
        "--submitter-username <username>",
        "--commit <sha1>",
        "--newrev <sha1>",
    ]

    CHANGE_ABANDONED = [
        "--change <change id>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--topic <topic>",
        "--abandoner <abandoner>",
        "--abandoner-username <username>",
        "--commit <sha1>",
        "--reason <reason>",
    ]

    CHANGE_DELETED = [
        "--change <change id>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--project <project name>",
        "--branch <branch>",
        "--topic <topic>",
        "--deleter <deleter>",
    ]

    CHANGE_RESTORED = [
        "--change <change id>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--topic <topic>",
        "--restorer <restorer>",
        "--restorer-username <username>",
        "--commit <sha1>",
        "--reason <reason>",
    ]

    REF_UPDATED = [
        "--oldrev <old rev>",
        "--newrev <new rev>",
        "--refname <ref name>",
        "--project <project name>",
        "--submitter <submitter>",
        "--submitter-username <username>",
    ]

    PROJECT_CREATED = [
        "--project <project name>",
        "--head <head name>"
    ]

    REVIEWER_ADDED = [
        "--change <change id>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--reviewer <reviewer>",
        "--reviewer-username <username>",
    ]

    REVIEWER_DELETED = [
        "--change <change id>",
        "--change-url <change url>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--reviewer <reviewer>",
        "--Code-Review <score>",
    ]

    TOPIC_CHANGED = [
        "--change <change id>"
        "--change-owner <change owner>",
        "--change-owner-username <username>"
        "--project <project name>",
        "--branch <branch>"
        "--changer <changer>"
        "--changer-username <username>",
        "--old-topic <old topic>"
        "--new-topic <new topic>",
    ]

    HASHTAGS_CHANGED = [
        "--change <change id>",
        "--change-owner <change owner>",
        "--change-owner-username <username>",
        "--project <project name>",
        "--branch <branch>",
        "--editor <editor>",
        "--editor-username <username>",
        "--added <hashtag>",
        "--removed <hashtag>",
        "--hashtag <hashtag>",
    ]

    CLA_SIGNED = [
        "--submitter <submitter>",
        "--user-id <user_id>",
        "--cla-id <cla_id>",
    ]

    __all__ = [
        REF_UPDATE, REF_UPDATED, PATCHSET_CREATED, CLA_SIGNED, TOPIC_CHANGED,
        PROJECT_CREATED, REVIEWER_ADDED, REVIEWER_DELETED, HASHTAGS_CHANGED,
        CHANGE_ABANDONED, CHANGE_MERGED, CHANGE_DELETED, CHANGE_RESTORED, COMMENT_ADDED,
        COMMIT_RECEIVED, SUBMIT,
    ]

    def add_approval_category(self, label):
        """Extend the comment-added hooks flags with the given custom label.

        :param str label: The label of the approval category to add.
        """
        label_new_value = "--{} <score>".format(label)
        label_old_value = "--{}-oldValue <score>".format(label)
        self.COMMENT_ADDED += [label_new_value, label_old_value]

    def __getitem__(self, item):
        """Return the flags for the given hook name as a dict.

        The values of the dict are tuples - the option name as a string, and the
        configuration as a dict. The dict is only populated if special
        configurations are required. It must consist of valid kwargs for
        :meth:`argparse.ArgumentParser.add_argument`.

        :param str item: name of the hook to look up flags for.
        :raises KeyError: If the hook cannot be found.
        :rtype: Dict[str, Tuple[str, Dict]]
        """
        flag_list = super(HookFlagDefinitions, self).__getitem__(item)
        flag_configuration = {}
        for flag_string in flag_list:
            match = self.FLAG_PATTERN.match(flag_string)
            flag, description = match.group('flag'), match.group('description')
            options = FLAG_OPTIONS.get(flag[2:].upper(), default={})
            flag_configuration[flag] = description, options
        return flag_configuration


FLAGS = HookFlagDefinitions()
