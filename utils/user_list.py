# %%
from IPython.display import display
import pandas as pd


class GetList(object):
    def __init__(self):
        self.df_selfintro_users_status = pd.read_csv(
            'input/selfintro_users_status.csv')

    def selfintro_users_all(self):
        selfintro_users_all_list = [
            i for i in self.df_selfintro_users_status['user']]
        return selfintro_users_all_list

    def selfintro_users_rank(self, rank):
        selfintro_users_rank_list = [
            i for i in self.df_selfintro_users_status[self.df_selfintro_users_status['rank'] == rank]['user']]
        return selfintro_users_rank_list

    def selfintro_users_enroll(self, flag):
        selfintro_users_enroll_list = [
            i for i in self.df_selfintro_users_status[self.df_selfintro_users_status['enroll'] == flag]['user']]
        return selfintro_users_enroll_list

    def selfintro_users_enroll_rank(self, rank, enroll):
        selfintro_users_enroll_rank_list = [
            i for i in self.df_selfintro_users_status[
                (self.df_selfintro_users_status['rank'] == rank) & (self.df_selfintro_users_status['enroll'] == enroll)]['user']]
        return selfintro_users_enroll_rank_list


if __name__ == '__main__':
    get_list = GetList()
    # selfintro_users_all_list = get_list.selfintro_users_all()
    # print(selfintro_users_all_list)

    # selfintro_users_a_list = get_list.selfintro_users_rank('a')
    # print(selfintro_users_a_list)
    # print(len(selfintro_users_a_list))

    # selfintro_users_a_list = get_list.selfintro_users_enroll(0)
    # print(selfintro_users_a_list)
    # print(len(selfintro_users_a_list))

    selfintro_users_enroll_rank_list = get_list.selfintro_users_enroll_rank(
        'b', 0)
    print(selfintro_users_enroll_rank_list)
    print(len(selfintro_users_enroll_rank_list))
# %%
