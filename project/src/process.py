import pandas as pd
from sklearn.preprocessing import LabelEncoder
import yaml

def load_and_preprocess():
    with open('params.yaml') as f:
        params = yaml.safe_load(f)
    
    # Load the data
    df = pd.read_csv(params['data_source'], header=None)
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    # Encode labels
    le = LabelEncoder()
    df['species'] = le.fit_transform(df['species'])

    # Save processed data
    df.to_csv('./data/processed_iris.csv', index=False)
    return df

if __name__ == "__main__":
    
    processed_df = load_and_preprocess()
    print(processed_df.head())