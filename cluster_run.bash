git clone https://github.com/fenglinglwb/MAT.git
cd MAT

conda activate MAT_env

pip install -r requirements.txt

# Download pretrained model
if [ -f Places_512.pkl ]; then
    echo "File already exists, skipping download"
else
    echo "Downloading file..."
    curl -L -o Places_512.pkl "https://mycuhk-my.sharepoint.com/personal/1155137927_link_cuhk_edu_hk/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2F1155137927%5Flink%5Fcuhk%5Fedu%5Fhk%2FDocuments%2FRelease%2FMAT%2Fmodels%2FPlaces%5F512%2Epkl"
fi

# Run MAT
python MAT/generate_image.py --network Places_512.pkl --dpath images --mpath masks --outdir samples