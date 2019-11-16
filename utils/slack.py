# %%
import json
import os
import requests
import sys

from dotenv import load_dotenv


class SlackAPI(object):
    def __init__(self):
        self.url = 'https://slack.com/api/'

        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.params = {
            'token': os.environ.get('SLACK_API_TOKEN')
        }
        print(self.params)

    def call(self, method):
        """
        apiをpostでコールしjsonに変換して返却する。

        Parameters
        ----------
        method : str
            'https://slack.com/api/'に続けるメソッド名
            ex.) 'channels.history', 'users.list'

        Returns
        -------
        res_json : dict
            レスポンスをstr=>dict(json)に変換たもの
        """

        try:
            res = requests.post(self.url + method, params=self.params)
            res_json = res.json()
            print(res_json)
            return res_json
        except:
            print('取得できませんでした')
            sys.exit()


# %%
""" debug """
if __name__ == '__main__':
    import pandas as pd
    from IPython.display import display

    slack_api = SlackAPI()
    # slack_api = slack.SlackAPI()

    channels_list = slack_api.call('channels.list')['channels']
    channels_df = pd.DataFrame(data=channels_list)
    display(channels_df.head())

    users_list = slack_api.call('users.list')['members']
    users_df = pd.DataFrame(data=users_list)
    display(users_df.head())

    print(channels_df.shape)
    print(users_df.shape)
