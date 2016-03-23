# -*- coding: utf-8 -*-
from .GitHubAPI import GitHubAPI


class GitHubRepository:
    def __init__(self, api):
        self.api = api

    def fetch_commits(self):
        return self.api.fetch_commits()


## ============================================================

class Test:
    def run(self):
        self.test_fetch_commits()

    def test_fetch_commits(self):
        api = GitHubAPI()
        commits = GitHubRepository(api).fetch_commits()

        assert commits is not None
        assert len(commits) > 0


if __name__ == "__main__":
    Test().run()
