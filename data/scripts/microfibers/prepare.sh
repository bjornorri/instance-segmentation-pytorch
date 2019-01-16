# 1. Split into training and validation sets.
echo "1. Splitting into training and validation sets"
python 1-split_data.py

# 2. Create Semantic and Instance Masks.
echo "2. Creating semantic and instance masks"
python 1-create_annotations.py

# 3. Get Image Paths.
echo "3. Saving image paths"
python 2-get_image_paths.py

# 4. Get Image Shapes.
echo "4. Calculating image shapes"
python 2-get_image_shapes.py

# 5. Get Image Means and Standard Deviations.
echo "5. Calculating means and standard deviations per channel"
python 2-get_image_means-stds.py

# 6. Get Number of Instances.
echo "6. Calculating number of instances in images"
python 2-get_number_of_instances.py

# 7. Create LMDB.
echo "7. Creating LMDB"
python 3-create_dataset.py
