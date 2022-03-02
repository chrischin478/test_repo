app_dup_cols_dict = {
    "firstName": [
        "firstName",
        "first_name_2",
        "first_name_3"
        ],
    "lastName": [
        "lastName",
        "last_name"
    ]
}

app_cols = ["col1","firstName","firstName","new_col","firstName","col2","lastName","lastName","col3"]

def set_header(df_cols_list, dup_cols_dict):
    for idx, c in enumerate(df_cols_list):
        if c in dup_cols_dict:
            new_col_name = dup_cols_dict[c].pop(0)
            df_cols_list[idx] = new_col_name
    return df_cols_list

app_cols = set_header(app_cols, app_dup_cols_dict)
print(app_cols)