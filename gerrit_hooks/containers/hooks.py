"""Container class for the gerrit-hooks library.

Supplies containers which store supported hooks, as well as flag definitions.
"""
from gerrit_hooks.containers.base import Container


class SupportedHooks(Container):
    """Container class for supported hooks."""

    REF_UPDATE = "ref-update"
    COMMIT_RECEIVED = "commit-received"
    SUBMIT = "submit"
    PATCHSET_CREATED = "patchset-created"
    COMMENT_ADDED = "comment-added"
    CHANGE_MERGED = "change-merged"
    CHANGE_ABANDONED = "change-abandoned"
    CHANGE_DELETED = "change-deleted"
    CHANGE_RESTORED = "change-restored"
    REF_UPDATED = "ref-updated"
    PROJECT_CREATED = "project-created"
    REVIEWER_ADDED = "reviewer-added"
    REVIEWER_DELETED = "reviewer-deleted"
    TOPIC_CHANGED = "topic-changed"
    HASHTAGS_CHANGED = "hashtags-changed"
    CLA_SIGNED = "cla-signed"

    __all__ = [
        REF_UPDATE, REF_UPDATED, PATCHSET_CREATED, CLA_SIGNED, TOPIC_CHANGED,
        PROJECT_CREATED, REVIEWER_ADDED, REVIEWER_DELETED, HASHTAGS_CHANGED,
        CHANGE_ABANDONED, CHANGE_MERGED, CHANGE_RESTORED, COMMENT_ADDED,
        COMMIT_RECEIVED, SUBMIT, CHANGE_DELETED
    ]


HOOKS = SupportedHooks()
