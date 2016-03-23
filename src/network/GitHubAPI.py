# -*- coding: utf-8 -*-
import json
from http import HTTPStatus
from http import client


class GitHubAPI:
    def fetch_commits(self):
        headers = {
            'User-Agent': 'Dancing robot v0.0.0'
        }

        connection = client.HTTPSConnection('api.github.com')
        connection.request('GET', '/repos/gokhanbarisaker/dancingrobot-client/commits', None, headers)
        response = connection.getresponse()

        if (response.status == HTTPStatus.OK):
            ## TODO: Use streaming parser
            commits = json.loads(response.read().decode())

        connection.close()

        return commits


## ============================================================

class Test(object):
    def run(self):
        self.test_fetch_commits()

    def test_fetch_commits(self):
        commits = GitHubAPI().fetch_commits()

        assert commits is not None
        assert len(commits) > 0


# Test().run()
