import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 导入数据
ratings = pd.read_csv(r'作业\电影智能推荐\ratings.csv')
movies = pd.read_csv(r'作业\电影智能推荐\movies.csv')

# 筛选出评分大于3的记录
high_ratings = ratings[ratings['rating'] > 3]

# 将电影ID和用户ID进行聚合，得到每个用户看过的电影列表
user_movie_lists = high_ratings.groupby('userId')['movieId'].apply(list).reset_index()
user_movie_lists.columns = ['userId', 'movies_watched']

# 将用户看过的电影列表转换成布尔矩阵
te = TransactionEncoder()
te_ary = te.fit_transform(user_movie_lists['movies_watched'])
df_bool = pd.DataFrame(te_ary, columns=te.columns_)

# 使用 apriori 算法进行频繁项集挖掘
frequent_itemsets = apriori(df_bool, min_support=0.05, use_colnames=True)

# 生成关联规则
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

def get_recommendations(watched_movies, rules):
    recommendations = set()
    watched_movies = watched_movies[0] if isinstance(watched_movies, np.ndarray) else watched_movies
    for movie in watched_movies:
        recs = rules[rules['antecedents'] == frozenset([movie])]['consequents']
        for rec in recs:
            recommendations.update(rec)
    recommendations -= set(watched_movies)  # 去掉已经看过的电影
    return list(recommendations)

# 示例用户的电影推荐
example_user_id = 2  # 假设我们要为用户ID为2的用户推荐电影
example_user_movies = user_movie_lists[user_movie_lists['userId'] == example_user_id]['movies_watched'].values
recommended_movies = get_recommendations(example_user_movies, rules)

# 转换电影ID为电影名字
recommended_movie_names = movies[movies['movieId'].isin(recommended_movies)]['title'].values
print(f"为用户 {example_user_id} 推荐的电影: {recommended_movie_names}")