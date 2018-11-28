Install MPI
	$ sudo apt install mpich  

Create virtualenv (optional):  
	$ virtualenv env -p python3  
	$ source env/bin/activate  

Install requirements:  
	$ (env) pip3 install -r requirements.txt  

Run code (add flags for running in cluster):  
	$ (env) mpirun -n 4 python3 weird_puzzle.py