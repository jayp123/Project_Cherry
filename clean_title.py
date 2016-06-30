mojo_df=mojo_df.dropna(subset=["title"])
mojo_df['cln_title']=pd.DataFrame(map(lambda x: re.sub('[^a-zA-Z0-9]','',x), mojo_df["title"]))
meta_df=mojo_df.dropna(subset=["title"])
meta_df['cln_title']=pd.DataFrame(map(lambda x: re.sub('[^a-zA-Z0-9]','',x), meta_df["title"]))
