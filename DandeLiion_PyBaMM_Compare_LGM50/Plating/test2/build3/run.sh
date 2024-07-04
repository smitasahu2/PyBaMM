cp ../scripts/generate_json_LGM50.py .
python3 generate_json_LGM50.py

OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 ./dandeliion-core
