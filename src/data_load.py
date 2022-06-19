#데이터 로드 as dataframe & 간략한 정보
import pandas as pd

def load(trans, id, join_df):
<<<<<<< HEAD
#1. trans only
=======
    if trans & id:
        if join_df:
            df_trans = pd.read_csv('./0615_train_pp_ver1.csv')
            df_id = pd.read_csv('./train_identity.csv')
            df_merged = pd.merge(df_id, df_trans, how="outer", on='TransactionID')
            print(df_merged.describe())
            return df_merged
        else:
            df_merged = pd.merge(df_id, df_trans, how="inner", on='TransactionID')
            print(df_merged.describe())
            return df_merged

    # trans only
>>>>>>> 33d995f (temp2 branch fetched)
    if trans:
        df_trans = pd.read_csv('./0615_train_pp_ver1.csv')
        print(df_trans.describe())
        return df_trans
<<<<<<< HEAD
#2. id

=======
    # id only
>>>>>>> 33d995f (temp2 branch fetched)
    if id:
        df_id = pd.read_csv('./train_identity.csv')
        print(df_id.describe())

        return df_id
<<<<<<< HEAD
#3. id_trans table with inner join
    if join_df == 'outer ':
        df_merged_right = pd.merge(df_id, df, how="inner", on = 'TransactionID')
        print(df_merged_right.describe())
        return df_merged_right
    if join_df:
        df_merged_right = pd.merge(df_id, df, how="outer", on = 'TransactionID')
        print(df_merged_right.describe())
        return df_merged_right
=======
#3. id_trans table, default = outer join
>>>>>>> 33d995f (temp2 branch fetched)
