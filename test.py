import pandas as pd
target_user = pd.read_csv(f'target_user.csv',encoding="utf-8")
target_user = target_user[target_user['user_name'] == "nipponichi8"]["folder_name"].reset_index(drop=True)

