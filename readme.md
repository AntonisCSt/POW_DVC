# Project of the Week: DVC 
by DataTalksClub


## Installation
https://dvc.org/doc/install

## Initialize DVC

```bash
$ dvc init
Initialized DVC repository.

You can now commit the changes to git.

+---------------------------------------------------------------------+
|                                                                     |
|        DVC has enabled anonymous aggregate usage analytics.         |
|     Read the analytics documentation (and how to opt-out) here:     |
|             <https://dvc.org/doc/user-guide/analytics>              |
|                                                                     |
+---------------------------------------------------------------------+

What's next?
------------
- Check out the documentation: <https://dvc.org/doc>
- Get help and share ideas: <https://dvc.org/chat>
- Star us on GitHub: <https://github.com/iterative/dvc>
```

## Download data


`curl https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data -o iris.csv`

(used gitbash on windows11)

store it in `/data` folder/directory



## DVC tutorial

first we run `dvc init`
We don't want to push the dataset to git because it is not scalable. We can add remote storage if we want 
`dvc add data/iris.csv`

```bash
$ dvc add data/iris.csv
100% Adding...|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████|1/1 [00:00,  7.85file/s]

To track the changes with git, run:

        git add 'data\.gitignore' 'data\iris.csv.dvc'

To enable auto staging, run:

        dvc config core.autostage true
```

and we add,commit and push the `iris.csv.dvc` to our code repository (not that `iris.csv` is now ignored with .gitignore)
That's the beauty of dvc, we now just pushed the hash and not the actual file.

We actually now created a data repository!

## Updating dataset

Let's make a change. After some time let's say we add a new line in `data/iris.csv`:
`5.4,2.5,3.3,1.2,Iris-versicolor`

dvc should have detected that we changed a file like git, so if we run `dvc status` we get:

```bash
$ dvc status
data\iris.csv.dvc:
        changed outs:
                modified:           data\iris.csv
```

so we add it again:

```bash
dvc add data/iris.csv
100% Adding...|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████|1/1 [00:00, 12.31file/s]

To track the changes with git, run:

        git add 'data\iris.csv.dvc'

To enable auto staging, run:

        dvc config core.autostage true
```

git now should detect that iris.csv.dvc has changed since the data is different and thus the hash has changed.

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   data/iris.csv.dvc
```

now let's commit, and push to our repo and learn how to access the previous ones:

## Connect with remote storage


We could also add a storage remotely
`dvc remote add local /tmp/dvc-storage`
 and push it with
`dvc push -r local`

For simplicity let's create the 'remote' storage in a local file `mkdir /tmp/dvcstore`

and add it with:
`dvc remote add -d myremote ./tmp/dvcstore`

use `dvc pull` to get your data. Usually we run it after git pull or git clone. (as the dvc guide mentions).

## Accessing previous version datasets

git checkout HEAD~1 data/iris.csv.dvc

then dvc checkout and pull

# Data Pipelines

Let's create some stages which going to be a part of out ml pipeline.

we going to use the command:

```
dvc stage add   -n process \
                -p data_source,processed_data_source \
                -d src/process.py -d data/iris.csv \
                -o data/processed \
                python src/process.py
```

Once you've added a stage, you can run the pipeline with `dvc repro`.

let's add also the training stage:

```
dvc stage add   -n training \
                -p n_estimators,random_state,processed_data_source,model_path \
                -d src/process.py -d data/processed/processed_iris.csv \
                -o model/model.pkl \
                python src/training.py
```

running `dvc dag` we get:
```bash
+-------------------+  
| data/iris.csv.dvc |  
+-------------------+  
          *            
          *            
          *            
     +---------+       
     | process |       
     +---------+       
          *            
          *            
          *            
    +----------+       
    | training |       
    +----------+       
```

let's commit our work and continue with Metrics, Plots, and Parameters

## Metrics, Plots, and Parameters



#### Delete cash

``
 
 Questions: How to change between data versions???



Troubleshoot:

1) If you get this error, might want to add a version control like git (`git init`)

```bash
ERROR: failed to initiate DVC - C:\Users\AX-St\MyGIthub\POW_DVC is not tracked by any supported SCM tool (e.g. Git). Use `--no-scm` if you don't want to use any SCM or `--subdir` if initializing inside a subdirectory of a parent SCM repository.
```