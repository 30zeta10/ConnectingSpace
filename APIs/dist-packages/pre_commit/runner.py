from __future__ import unicode_literals

import os.path

from cached_property import cached_property

from pre_commit import git
from pre_commit.clientlib import load_config
from pre_commit.repository import Repository
from pre_commit.store import Store


class Runner(object):
    """A `Runner` represents the execution context of the hooks.  Notably the
    repository under test.
    """

    def __init__(self, git_root, config_file, store_dir=None):
        self.git_root = git_root
        self.config_file = config_file
        self._store_dir = store_dir

    @classmethod
    def create(cls, config_file):
        """Creates a Runner by doing the following:
            - Finds the root of the current git repository
            - chdir to that directory
        """
        root = git.get_root()
        os.chdir(root)
        return cls(root, config_file)

    @cached_property
    def git_dir(self):
        return git.get_git_dir(self.git_root)

    @cached_property
    def config_file_path(self):
        return os.path.join(self.git_root, self.config_file)

    @cached_property
    def config(self):
        return load_config(self.config_file_path)

    @cached_property
    def repositories(self):
        """Returns a tuple of the configured repositories."""
        repos = self.config['repos']
        return tuple(Repository.create(x, self.store) for x in repos)

    def get_hook_path(self, hook_type):
        return os.path.join(self.git_dir, 'hooks', hook_type)

    @cached_property
    def pre_commit_path(self):
        return self.get_hook_path('pre-commit')

    @cached_property
    def pre_push_path(self):
        return self.get_hook_path('pre-push')

    @cached_property
    def store(self):
        return Store(self._store_dir)
