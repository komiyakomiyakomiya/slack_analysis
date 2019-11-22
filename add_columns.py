# %%
import numpy as np
import pandas as pd
import japanize_matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


from utils import user_list
from utils import dictionary

# インスタンス作成
df = pd.read_csv('input/talk_20191116.csv')
# インスタンス作成
get_list = user_list.GetList()
get_dict = dictionary.GetDict()
# %%
"""
継続 == 1
退会 == 0
"""
enroll_users_list = get_list.enroll_users()

df['enroll'] = [1 if i in enroll_users_list else 0 for i in df['talk_user']]

display(df['enroll'])

# %%
active_rank_dict = get_dict.active_rank()
# print(active_rank_dict)
print(active_rank_dict)

df['rank'] = df['talk_user'].copy()
display(df['rank'])
df['rank'] = df['rank'].map(active_rank_dict)
df['rank'] = df['rank'].fillna('D')
# print(['D' if i == nan else i for i in df['rank']])
# print([i for i in df['rank'] if i == False])
# df['rank'] = ['D' if i == 'nan' else i for i in df['rank']]
display(df['rank'])
# df[df['rank'] == 'NaN']


# %%
df.('output/talk_df_add_enroll_rank.csv')

# %%
# %%
offline_set = {
    '村上 智之',
    'nishioka kenichi',
    'Satoru Mikami',
    'banquet.kuma',
    'Katsuya Nagano',
    '尾銭泰徳 ozeni.yasunori',
    'Komiya',
    'はやと-休学中の文系学生',
    '吉村　政彦',
    '澤祐斗',
    'sota_sakuma',
    'Maho Uchida',
    'yuji.imuta',
    '清重 愛一郎',
    'Kotaro Isobe',
    '岸田 凌',
    '杉本　光一',
    'れごん',
    '上畑 安須輝',
    'たぎｰ',
    'Yam ',
    'SHINNOSUKE KOTAKE',
    'seiyakitazume',
    'akumi6 ',
    '笹尾卓史',
    'Yumi.M',
    'S',
    'Soliton0929',
    'Kotaro Fukushima',
    'junpe',
    'Vo Nhat Huy',
    'Tasuku Sato'
}

df_off = df.copy()
df_off['join_offline'] = 0
for i in range(len(df_off['join_offline'])):
    if df_off['talk_user'][i] in offline_set:
        df_off['join_offline'][i] = 1


# %%
df_off.to_csv('output/offline.csv')


# %%
df_status = pd.read_csv('input/selfintro_users_status.csv')
df_status['join_offline'] = 0
for i in range(len(df_status['join_offline'])):
    if df_status['user'][i] in offline_set:
        df_status['join_offline'][i] = 1

display(pd.crosstab(df_status['rank'], df_status['join_offline']))
display(pd.crosstab(df_status['rank'],
                    df_status['join_offline'], normalize='index'))

sns.countplot(x='rank', hue='join_offline', data=df_status)
plt.title('オフ会参加経験とアクティブランク')
plt.xticks([0, 1, 2], ['アクティブ', '準アクティブ', '非アクティブ'])
plt.legend(['参加経験アリ', '参加経験ナシ'])
plt.show()
# %%
df_off.to_csv('output/users_status.csv')

# %%
