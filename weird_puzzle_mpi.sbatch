#!/bin/bash
#
#SBATCH --partition=piv
#SBATCH --job-name=weird_puzzle_py
#SBATCH --time=10:00
#SBATCH --output=weird_puzzle_py.%j.out
#SBATCH --ntasks=5
#

echo "----------Preparando el entorno-------------"
module purge
module load --ignore-cache prun gnu7/7.3.0 openmpi3 py3-mpi4py
source env/bin/activate
pip install -r requirements.txt

echo "-------Inicio de Proceso en mpi Python------"
python weird_puzzle.py < test.in
echo "-------Fin de Proceso en mpi Python------"
