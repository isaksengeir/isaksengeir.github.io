# HPC cheats
[MAS](https://metacenter.no)

[Monitoring jobs](https://documentation.sigma2.no/jobs/monitoring.html)

[SACCT](https://slurm.schedmd.com/sacct.html)

## Daily first-line randoms
<i>"hmm, how did I do that again?"</i>
For now, I will just throw these in here in a random fashion. Maybe categorize later ....

### Modifying / viewing jobs ('scontrol')
#### Extend wall-time
`scontrol update jobId 12345 TimeLimit=4-00:00:00` 

#### Change --account for job in queue
`scontrol update jobid=<ID> account=<new acc> qos=<new acc>`

#### Get job info
`scontrol show job <jobbid> --details | grep Nodes`


### Get node information:
`scontrol --oneliner show node` <-- one line per node. Remove this to get print over several lines.

### How much memory has a job used ? 
`sacct -j 2138531 --format=MaxRSS` ([SACCT](https://slurm.schedmd.com/sacct.html))

### Search for files for user in project
- `find $USERWORK -type f -group $PROJECT`
- `find $USERHOME -type f -group $PROJECT`
- `lfs quota -g $PROJECT /cluster`
- `rbh-du (robin hood -- can be delay)`
- `lfs find /cluster/home/ -type f --group nn1234k`  (LUSTRE)


### Test misbehaving software 
*strace* is useful for debugging. Example here with gaussian:


`strace -f -e trace=%process,open,stat -o strace.log g16.ib \$input.com > \$input.out`

## Modules (lua)
### Custom modules 
You can do your own modules, say under HOME/my_modules. Then, you can make them available for module commands by running `module use -a $HOME/my_modules.`

### Show hidde modules
`module --show-hidden avail`

## Node cpu core/task
Node --> CPU(s) --> Core(s)/tasks
- A node is the physical box containing a computer
  - Has unique hostname and set of running processes
- The motherboard in each node can have several sockets and thus a cpu chip in each sockeet
- Each CPU has multiple cores

- Node is a compute node (one computer)
- CPU is a processor inside a node. There are 2 CPUS per node. This is also called a socket
- Core is a processing unit inside a CPU. This differs for each system and you can check with the command <mark>freepe</mark> to get a list of all the variations and how much is free at a given time.

### sbatch options
* --nodes: nodes/machines
* --ntasks: MPI tasks or processes, equal to “cores” only when “cpus-per-task” is set to one
* --cpus-per-tasks: number of cores per task/process
* --mem-per-cpu: memory per core
* --mem: memory per node

If a program accepts an option called -threads, it typically refers to shared memory (OpenMP etc) which relates to the --cpus-per-task option in sbatch.
