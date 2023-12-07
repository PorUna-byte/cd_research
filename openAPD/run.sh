# python tools/train.py configs/pcam/pcam_r18_512x512_4k_flaw.py  --work-dir ./pcam_r18_flaw_workdir  --gpu-id 0  --seed 307

# get .png results
python tools/test.py configs/pcam/pcam_r18_512x512_4k_flaw.py   pcam_r18_flaw_workdir/latest.pth --format-only --eval-options "imgfile_prefix=tmp_infer" --gpu-id 0 
# get metrics
python tools/test.py configs/pcam/pcam_r18_512x512_4k_flaw.py   pcam_r18_flaw_workdir/latest.pth --eval mFscore mIoU --gpu-id 0 