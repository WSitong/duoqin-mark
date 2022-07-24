import os.path

path_share = 'root'
app_dir = os.path.dirname(__file__)
full_path_share = os.path.join(app_dir, path_share)

if not os.path.exists(full_path_share):
    os.mkdir(full_path_share)
