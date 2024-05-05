
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

We could also add a storage remotely and push it with `dvc push` but we are not going to do that now.

Let's make a change. After some time let's say we add a new line:
