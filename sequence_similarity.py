import pandas as pd


if __name__ == "__main__":
    databases = ["uspto", "swissprot", "thpdb", "paper"]
    dfs = []
    for database in databases:
        df["db"] = database
        df = pd.read_csv(f"{database}.m8", sep="\t", header=None)
        df = df[[0, 1, 2, 3, 4, 5, 6]]
        df.columns = ["id", "db_id", "identity", "alignment_length", "num_mismatches", "query_coverage", "target_coverage"]
        df.sort_values("identity", ascending=False).drop_duplicates("id")
        dfs.append(df)
        
    df = pd.concat(dfs)
    df["similarity_check"] = df["identity"] * df["query_coverage"]
    df = df.sort_values("similarity_check", ascending=False).drop_duplicates("id")
    df.to_csv("sequence_similarity.csv", index=False)
