#### Usando MPICH
Install MPI  
	$ sudo apt install mpich  

Create virtualenv (optional):  
	$ virtualenv env -p python3  
	$ source env/bin/activate  

Install requirements:  
	$ (env) pip3 install -r requirements.txt  

Run code (add flags for running in cluster):  
	$ (env) mpirun -n 4 python3 weird_puzzle.py < test.in

#### USANDO Slurm
Enviamos el Job con:
	$ sbatch  weird_puzzle_mpi.sbatch
	
Por defecto, usa como entrada test.in, puede cambiarse en weird_puzzle_mpi.sbatch
