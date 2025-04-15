import os
import requests
from pathlib import Path
import platform

system_type = platform.system()

import yaml
with open("config.yaml", "r") as f:
  config = yaml.safe_load(f)

n_subjects = config["N_SUBJECTS"]
n_runs = 1  #config["N_RUNS"]
zenodo_id = config["ZENODO_ID"]
gdf_dir = config["GDF_DIR"]
mat_dir = config["MAT_DIR"]

gdf_dir = Path(gdf_dir).expanduser().resolve()
mat_dir = Path(mat_dir).expanduser().resolve()

def make_gdf_link(subject, run, imagery=False):
  assert "n_subjects" in globals()
  assert "n_runs" in globals()
  assert "zenodo_id" in globals()

  if subject==0 or subject>n_subjects:
    raise(ValueError("Invalid subject number"))
  if run==0 or run>n_runs:
    raise(ValueError("Invalid run number"))

  if imagery==False:
    return f"https://zenodo.org/records/{zenodo_id}/files/motorexecution_subject{subject}_run{run}.gdf?download=1"
  else:
    return f"https://zenodo.org/records/{zenodo_id}/files/motorimagination_subject{subject}_run{run}.gdf?download=1"

def download_gdf(subject, run, imagery=False):
  assert "gdf_dir" in globals()
  gdf_link = make_gdf_link(subject, run, imagery)
  
  if imagery==False:
    filename = f"motorexecution_subject{subject}_run{run}.gdf"
  else:
    filename = f"motorimagination_subject{subject}_run{run}.gdf"

  if os.path.exists(os.path.join(mat_dir, f"{filename[:-4]}.mat")) or\
    os.path.exists(os.path.join(gdf_dir, filename)):
    print(f"{filename} already processed")
    return
  else:
    dir = os.path.join(gdf_dir, filename)
    print(f"Downloading {filename}")
    response = requests.get(gdf_link)
    with open(dir, "wb") as f:
      f.write(response.content)
    return

if __name__ == '__main__':
    for subject in range(1, n_subjects+1):
        for run in range(1, n_runs+1):
            download_gdf(subject, run)