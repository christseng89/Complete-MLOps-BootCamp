import pandas as pd
import os
import whylogs as why

os.environ["WHYLABS_DEFAULT_ORG_ID"] = "org-rE7D6t" # ORG-ID is case sensitive
os.environ["WHYLABS_API_KEY"] = "1YQ18PUd8J.f6TZX0zvGOOxjcINzP3xWoquAPaXSM7KZ9CtaklkLAuKLlILxuzHF:org-rE7D6t"
os.environ["WHYLABS_DEFAULT_DATASET_ID"] = "model-3" # The selected project "Model-1 (model-3)" is "model-3"

# Point to your local CSV if you have your own data
df = pd.read_csv("https://whylabs-public.s3.us-west-2.amazonaws.com/datasets/tour/current.csv")

#log dataframe
results = why.log(df)

#upload results to WhyLabs
results.writer("whylabs").write()