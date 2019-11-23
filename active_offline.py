# %%
import numpy as np
import pandas as pd
import japanize_matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


df_status = pd.read_csv('input/selfintro_users_status.csv')

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
    '澤 祐斗',
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
    'Yam',
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

df_status['join_offline'] = 0
for i in range(len(df_status['join_offline'])):
    # display(df_status.head())
    if df_status['user'][i] in offline_set:
        df_status['join_offline'][i] = 1

# %%
df_status
# %%
ignore_list = [
    'Slackbot',
    'GitHub',
    '村上 智之',
    '國分咲良',
    '岡村龍弥'
]
df_status.drop(
    df_status.index[df_status['user'].isin(ignore_list)], inplace=True)


display(pd.crosstab(df_status['rank'], df_status['join_offline']))
display(pd.crosstab(df_status['rank'],
                    df_status['join_offline'], normalize='index'))

sns.countplot(x='rank', hue='join_offline', data=df_status)
plt.title('オフ会参加経験とアクティブランク')
plt.xticks([0, 1, 2], ['アクティブ', '準アクティブ', '非アクティブ'])
plt.legend(['参加経験ナシ', '参加経験アリ'])
plt.show()
# %%
df_status.to_csv('output/users_status.csv')

# %%
df_status.head(60)

# %%
