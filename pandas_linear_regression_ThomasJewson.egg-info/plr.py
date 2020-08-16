def slope(df):
    """
    Outputs the regression line slope

    The x-axis of the returned DataFrame is the x-axis of the line.
    The y-axis of the returned DataFrame is the y-axis of the line.
    """

    def slope_x(df,x):
        def slope_single(df,x,y):
            return df.corr().loc[x,y] * df[y].std() / df[x].std()
        import pandas as pd
        out_df = pd.DataFrame(columns=[x])
        for z in range(len(df.corr())):
            part_df = pd.DataFrame(
                data = [slope_single(df,x,df.corr().columns[z])],
                columns = [x],
                index = [df.corr().columns[z]]
            )
            out_df = out_df.append(part_df)
        return out_df

    out_df = slope_x(df,df.corr().columns[0])
    for z in range(1,len(df.corr())):
        out_df = out_df.join(slope_x(df,df.corr().columns[z]))
    return out_df


def intercept(df):
    def intercept_single(df,x,y):
        def slope_single(df,x,y):
            return df.corr().loc[x,y] * df[y].std() / df[x].std()
        return df[y].mean() - (slope_single(df,x,y)*df[x].mean())
    out_df = slope(df)
    for x_ax in range(len(df.corr())):
        for y_ax in range(len(df.corr())):
            out_df.loc[df.corr().index[y_ax],df.corr().index[x_ax]] = intercept_single(df,df.corr().index[x_ax],df.corr().index[y_ax])
    return out_df


def predict(df,x,z):
    out_df = slope(df)*z+intercept(df)
    return out_df[x]
