#!/bin/bash -x

if [ "x$SLURM_NPROCS" = "x" ]
then
  if [ "x$SLURM_NTASKS_PER_NODE" = "x" ]
  then
    SLURM_NTASKS_PER_NODE=1
  fi
  SLURM_NPROCS=`expr $SLURM_JOB_NUM_NODES \* $SLURM_NTASKS_PER_NODE`
else
  if [ "x$SLURM_NTASKS_PER_NODE" = "x" ]
  then
    SLURM_NTASKS_PER_NODE=`expr $SLURM_NPROCS / $SLURM_JOB_NUM_NODES`
  fi
fi

srun hostname -s | sort -u > /tmp/hosts.$SLURM_JOB_ID
awk "{ print \$0 \" slots=$SLURM_NTASKS_PER_NODE\"; }" /tmp/hosts.$SLURM_JOB_ID >/tmp/tmp.$SLURM_JOB_ID
mv /tmp/tmp.$SLURM_JOB_ID /tmp/hosts.$SLURM_JOB_ID

cat /tmp/hosts.$SLURM_JOB_ID

module load xl_r
#module load cmake
module load spectrum-mpi
module load cuda

case=./in.restart.3900000
exe=/gpfs/u/home/FFPN/FFPNprbs/scratch/lammps-bump-sept/build/lmp_AiMOS_mark
mpirun -hostfile /tmp/hosts.$SLURM_JOB_ID -np $SLURM_NPROCS $exe -sf gpu -pk gpu 6 -in $case > $SLURM_JOB_ID.out

rm /tmp/hosts.$SLURM_JOB_ID
