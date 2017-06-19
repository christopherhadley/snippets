#Useful info on having multiple python enviornments running with anaconda: 
#https://conda.io/docs/py2or3.html

conda create --name py27 python=2.7
conda create --name py36 python=3.6

conda info --envs
conda env remove -n py27

source activate py27
source deactive py27

#You can add these to .bash_rc