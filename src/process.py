import pandas as pd
from sklearn.preprocessing import LabelEncoder 
import yaml
import os

def load_and_preprocess():
    with open('params.yaml') as f:
        params = yaml.safe_load(f)
    
    # Load the data
    df = pd.read_csv(params['data_source'], header=None)
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    # Encode labels
    le = LabelEncoder()
    df['species'] = le.fit_transform(df['species'])

    path = 'data/processed/'

    # Check if the directory already exists
    if not os.path.exists(path):
        # Create the directory if it doesn't exist
        os.makedirs(path)
        print("Folder created:", path)
    else:
        print("Folder already exists:", path)

    # Save processed data
    df.to_csv(params['processed_data_source'], index=False)
    
    return df

if __name__ == "__main__":
    
    processed_df = load_and_preprocess()
    print(processed_df.head())