import pandas as pd
import shutil
import os
 
# Path to your CSV file
csv_file = '/home/autoeval/phase1/img_model_answer_mapping.csv'
 
# Directory where images are stored
source_folder = '/home/autoeval/phase1/phase_1_eval_dataset_enc/phase_1_eval_dataset/'
 
# Read CSV into a DataFrame
df = pd.read_csv(csv_file)
print(df)
# Group by type_id and iterate over groups
for type_id, group in df.groupby('model_answer'):
    # Create a folder for each type_id if it doesn't exist
    target_folder = f'/home/autoeval/phase1/{type_id}/'
    os.makedirs(target_folder, exist_ok=True)
    # Iterate through images in this group
    for index, row in group.iterrows():
        image_path = row['img_name']
        source_path = os.path.join(source_folder, image_path)
        target_path = os.path.join(target_folder, image_path)
        # Move the image to the respective folder
        shutil.move(source_path, target_path)
        print(f'Moved {image_path} to {target_folder}')