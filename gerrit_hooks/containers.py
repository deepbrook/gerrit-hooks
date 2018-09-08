import re


class SupportedHooks:
    """Container class for supported hooks."""

    REF_UPDATE = "ref-update"
    COMMIT_RECEIVED = "commit-received"
    SUBMIT = "submit"
    PATCHSET_CREATED = "patchset-created"
    COMMENT_ADDED = "comment-added"
    CHANGE_MERGED = "change-merged"
    CHANGE_ABANDONED = "change-abandoned"
    CHANGE_RESTORED = "change-restored"
    REF_UPDATED = "ref-updated"
    PROJECT_CREATED = "project-created"
    REVIEWER_ADDED = "reviewer-added"
    REVIEWER_DELETED = "reviewer-deleted"
    TOPIC_CHANGED = "topic-changed"
    HASHTAGS_CHANGED = "hashtag-changed"
    CLA_SIGNED = "cla-signed"

    __all__ = [
        REF_UPDATE, REF_UPDATED, PATCHSET_CREATED, CLA_SIGNED, TOPIC_CHANGED,
        PROJECT_CREATED, REVIEWER_ADDED, REVIEWER_DELETED, HASHTAGS_CHANGED,
        CHANGE_ABANDONED, CHANGE_MERGED, CHANGE_RESTORED, COMMENT_ADDED,
        COMMIT_RECEIVED, SUBMIT,
    ]

    def __getitem__(self, item):
        return self.__all__[item]

    def __len__(self):
        return len(self.__all__)

    def __contains__(self, item):
        return item in self.__all__


class HookFlagDefinitions:
    """Container class for each supported hook's supported CLI flags."""

    # RegEx pattern to parse the flag strings contained in HookType class.
    FLAG_PATTERN = re.compile(r'(?P<flag>--(\w|-)*)\s(?P<description>\<(\w|-|\s)*\>)')

    REF_UPDATE_FLAGS = "--project <project name> --refname <refname> --uploader <uploader> " \
                       "--uploader-username <username> --oldrev <sha1> --newrev <sha1>"

    COMMIT_RECEIVED_FLAGS = "--project <project name> --refname <refname> " \
                            "--uploader <uploader> --uploader-username <username> " \
                            "--oldrev <sha1> --newrev <sha1> --cmdref <refname>"

    SUBMIT_FLAGS = "--project <project name> --branch <branch> --submitter <submitter> " \
                   "--patchset <patchset id> --commit <sha1>"

    # --kind may be one of:
    # REWORK, TRIVIAL_REBASE, MERGE_FIRST_PARENT_UPDATE, NO_CODE_CHANGE, NO_CHANGE
    PATCHSET_CREATED_FLAGS = "--change <change id> --kind <change kind> " \
                             "--change-url <change url> --change-owner <change owner> " \
                             "--change-owner-username <username> --project <project name> " \
                             "--branch <branch> --topic <topic> --uploader <uploader> " \
                             "--uploader-username <username> --commit <sha1> " \
                             "--patchset <patchset id>"

    COMMENT_ADDED_FLAGS = "--change <change id> --change-url <change url> " \
                          "--change-owner <change owner> --change-owner-username <username> " \
                          "--project <project name> --branch <branch> --topic <topic> " \
                          "--author <comment author> --author-username <username> " \
                          "--commit <commit> --comment <comment> " \
                        # These aren't currently supported!
                          "[--<approval category id> <score> " \
                          "--<approval category id> <score> " \
                          "--<approval category id>-oldValue <score> ...]"

    CHANGE_MERGED_FLAGS = "--change <change id> --change-url <change url> " \
                          "--change-owner <change owner> --change-owner-username <username> " \
                          "--project <project name> --branch <branch> --topic <topic> " \
                          "--submitter <submitter> --submitter-username <username> " \
                          "--commit <sha1> --newrev <sha1>"

    CHANGE_ABANDONED_FLAGS = "--change <change id> --change-url <change url> " \
                             "--change-owner <change owner> " \
                             "--change-owner-username <username> " \
                             "--project <project name> --branch <branch> " \
                             "--topic <topic> --abandoner <abandoner> " \
                             "--abandoner-username <username> --commit <sha1> " \
                             "--reason <reason>"

    CHANGE_RESTORED_FLAGS = "--change <change id> --change-url <change url> " \
                            "--change-owner <change owner> " \
                            "--change-owner-username <username> --project <project name> " \
                            "--branch <branch> --topic <topic> --restorer <restorer> " \
                            "--restorer-username <username> --commit <sha1> " \
                            "--reason <reason>"

    REF_UPDATED_FLAGS = "--oldrev <old rev> --newrev <new rev> --refname <ref name> " \
                        "--project <project name> --submitter <submitter> " \
                        "--submitter-username <username>"

    PROJECT_CREATED_FLAGS = "--project <project name> --head <head name>"

    REVIEWER_ADDED_FLAGS = "--change <change id> --change-url <change url> " \
                           "--change-owner <change owner> " \
                           "--change-owner-username <username> " \
                           "--project <project name> --branch <branch> " \
                           "--reviewer <reviewer> --reviewer-username <username>"

    REVIEWER_DELETED_FLAGS = "--change <change id> --change-url <change url> " \
                             "--change-owner <change owner> " \
                             "--change-owner-username <username> " \
                             "--project <project name> --branch <branch> " \
                             "--reviewer <reviewer> [--<approval category id> <score> " \
                             "--<approval category id> <score> ...]"

    TOPIC_CHANGED_FLAGS = "--change <change id> --change-owner <change owner> " \
                          "--change-owner-username <username> --project <project name> " \
                          "--branch <branch> --changer <changer> --changer-username <username> " \
                          "--old-topic <old topic> --new-topic <new topic>"

    # --hashtag, --added and --removed may be passed multiple times
    HASHTAGS_CHANGED_FLAGS = "--change <change id>  --change-owner <change owner> " \
                             "--change-owner-username <username> --project <project name> " \
                             "--branch <branch> --editor <editor> " \
                             "--editor-username <username> --added <hashtag> " \
                             "--removed <hashtag> --hashtag <hashtag>"

    CLA_SIGNED_FLAGS = "--submitter <submitter> --user-id <user_id> --cla-id <cla_id>"

    __all__ = [
        REF_UPDATE_FLAGS, REF_UPDATED_FLAGS, PATCHSET_CREATED_FLAGS, CLA_SIGNED_FLAGS, TOPIC_CHANGED_FLAGS,
        PROJECT_CREATED_FLAGS, REVIEWER_ADDED_FLAGS, REVIEWER_DELETED_FLAGS, HASHTAGS_CHANGED_FLAGS,
        CHANGE_ABANDONED_FLAGS, CHANGE_MERGED_FLAGS, CHANGE_RESTORED_FLAGS, COMMENT_ADDED_FLAGS,
        COMMIT_RECEIVED_FLAGS, SUBMIT_FLAGS,
    ]

    __mapping__ = {
        SupportedHooks.REF_UPDATE: REF_UPDATE_FLAGS,
        SupportedHooks.REF_UPDATED: REF_UPDATED_FLAGS,
        SupportedHooks.PATCHSET_CREATED: PATCHSET_CREATED_FLAGS,
        SupportedHooks.CLA_SIGNED: CLA_SIGNED_FLAGS,
        SupportedHooks.TOPIC_CHANGED: TOPIC_CHANGED_FLAGS,
        SupportedHooks.PROJECT_CREATED: PROJECT_CREATED_FLAGS,
        SupportedHooks.REVIEWER_ADDED: REVIEWER_ADDED_FLAGS,
        SupportedHooks.REVIEWER_DELETED: REVIEWER_DELETED_FLAGS,
        SupportedHooks.HASHTAGS_CHANGED: HASHTAGS_CHANGED_FLAGS,
        SupportedHooks.CHANGE_MERGED: CHANGE_MERGED_FLAGS,
        SupportedHooks.CHANGE_ABANDONED: CHANGE_ABANDONED_FLAGS,
        SupportedHooks.CHANGE_RESTORED: CHANGE_RESTORED_FLAGS,
        SupportedHooks.COMMENT_ADDED: COMMENT_ADDED_FLAGS,
        SupportedHooks.COMMIT_RECEIVED: COMMIT_RECEIVED_FLAGS,
        SupportedHooks.SUBMIT: SUBMIT_FLAGS
    }

    def __getitem__(self, item):
        """Return the flags for the given hook name as a dict.

        :param str item: name of the hook to look up flags for.
        :raises KeyError: If the item cannot be found.
        :rtype: Dict
        """
        flag_string = self.__mapping__[item]
        flag_configuration = {}
        for match in self.FLAG_PATTERN.finditer(flag_string):
            flag, description = match.flag, match.description
            options = {}
            if (flag in ('--hashtag', '--added', '--removed')
                    and item == SupportedHooks.HASHTAGS_CHANGED):
                # These flags may be passed several times; therefore, we need
                # to store them multiple times. The 'append' action appends
                # the passed value as a List[str] to the related flag variable
                # in the namespace. For example::
                #
                #   hashtag-changes --hashtag hello --hashtag wonky
                #
                # would result in ::
                #
                #   >>>options = parse_options()
                #   >>>options.hashtag
                #   [['hello'], ['wonky']]
                options.update({'nargs': '1', 'action': 'append'})
            flag_configuration[flag] = description, options
        return {
            match.flag: (match.description, {})
            for match in self.FLAG_PATTERN.finditer(flag_string)
        }
