# %%
import datetime

from IPython.display import display
import pandas as pd
import numpy as np


class GetDict(object):
    def __init__(self):
        self.df_talks = pd.read_csv('input/talks.csv', sep='\t')
        self.df_users = pd.read_csv('input/users.csv', sep='\t')
        self.df_comments_per_day = pd.read_csv(
            'input/comments_par_day.csv')
        self.df_enroll_users = pd.read_csv(
            'input/enroll_users.csv')
        self.df_selfintro = pd.read_csv('input/selfintro.csv')

    def _utc_to_jst(self, unix, format):
        """
        unix_timeをdatetime(JST)に変換し指定のフォーマットで返す。

        Parameters
        ----------
        unix: int
            unix time

        Returns
        -------
        timestamp_time: datetime.datetime
            datetime(JST)
        """
        # 日本のタイムゾーン
        JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
        # unix->datetime変換
        timestamp = datetime.datetime.fromtimestamp(unix, JST)
        # フォーマットを直すために一度strに変換
        timestamp_str = datetime.datetime.strftime(
            timestamp, format)
        timestamp_time = datetime.datetime.strptime(
            timestamp_str, format)
        return timestamp_time

    def users_id_name(self):
        # indexをuser_idに置き換え
        df_users_replace_index = self.df_users.set_index('user_id')

        # {index(user_id): real_name_normalized}のかたちで辞書を作成
        users_dict = df_users_replace_index['real_name_normalized'].to_dict()
        return users_dict

    def users_join_datetime(self, datetime_format):
        """
        Parameters
        ----------
        datetime_format: str
            ex.)
                '%Y%m%d%H%M%S'
                '%Y-%m-%d'
        """
        # ユーザーIDとユーザー名を紐付けたdictを作成
        users_dict = self.users_id_name()

        # generalのみ抽出
        df_talks_general = self.df_talks[self.df_talks['channel_id']
                                         == 'CJNKJ8JKW']

        # ['talk_user', 'text', 'ts']のみ抽出
        df_talks_extract = df_talks_general[['talk_user', 'text', 'ts']]

        # 欠損値がある行をおとす
        df_talks_dropna = df_talks_extract.dropna()

        # slackbotのチャンネル参加コメントを抽出
        # generalの参加コメントがコミュニティ参加日時になる
        df_talks_join_comment = df_talks_dropna[df_talks_dropna['text'].str.contains(
            '>さんがチャンネルに参加しました')]

        # self.df_talksのtalk_userカラムを登録名で置換
        df_talks_join_comment['talk_user'] = df_talks_join_comment['talk_user'].map(
            users_dict)

        display('####df_talks_join_comment####')
        display([i for i in df_talks_join_comment['talk_user']])

        # UNIXタイムをdatetimeに変換してカラムとして追加
        df_talks_join_comment['datetime'] = [self._utc_to_jst(
            unix, datetime_format) for unix in df_talks_join_comment['ts'].dropna()]

        # user_nameと登録日時を紐付けたdictをつくる
        df_talks_join_comment = df_talks_join_comment.set_index(
            'talk_user')

        user_join_time_dict = df_talks_join_comment['datetime'].to_dict()

        return user_join_time_dict

    def active_rank(self):
        df_comments_per_day_replace_index = self.df_comments_per_day.set_index(
            'talk_user')
        active_rank_dict = df_comments_per_day_replace_index['rank'].to_dict()
        return active_rank_dict

    def enroll_users(self):
        enroll_users_replace_index = self.df_enroll_users.set_index(
            'display_name_normalized')
        print(enroll_users_replace_index['flag'].sum())
        enroll_users_dict = enroll_users_replace_index['flag'].to_dict()
        return enroll_users_dict

    def self_intro(self):
        users_dict = self.users_id_name()
        # 自己紹介チャンネルのみ抽出
        df_self_intro = self.df_talks[self.df_talks['channel_id']
                                      == 'CJP6483K2']

        df_self_intro_dropna = df_self_intro.dropna()

        # 自己紹介チャンネルのみ抽出
        df_drop_join_comment = df_self_intro_dropna.query(
            'text not in "さんがチャンネルに参加しました"')

        df_self_intro_replace_user = df_drop_join_comment['talk_user'].map(
            users_dict)

        self_intro_dict = {i: 1 for i in df_self_intro_replace_user}

        return self_intro_dict

    def selfintro_datetime(self, datetime_format):
        user_name_set = set(i for i in self.df_selfintro['talk_user'])

        selfintro_dict = {}
        for name in user_name_set:
            df_personal = self.df_selfintro[self.df_selfintro['talk_user'] == name]
            selfintro_date_del_index = [i for i in df_personal['date']][0]
            selfintro_dict[name] = selfintro_date_del_index

        return selfintro_dict


if __name__ == '__main__':
    # debug
    get_dict = GetDict()
    # users_dict = get_dict.users_id_name()
    # print(users_dict)

    # join_dict = get_dict.users_join_datetime('%Y-%m-%d')
    # print(join_dict)

    active_rank_dict = get_dict.active_rank()
    print(active_rank_dict)

    # enroll_users_dict = get_dict.enroll_users()
    # print(enroll_users_dict)

    # self_intro_dict = get_dict.selfintro_datetime('%Y-%m-%d')
    # print(self_intro_dict)


# %%
