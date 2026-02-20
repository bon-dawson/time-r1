from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="Boshenxx/Time-R1-7B",
    local_dir="ckpts/Time-R1-7B",
    local_dir_use_symlinks=False
)