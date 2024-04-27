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

## Track files

To track then you can specify them explicitly:

`dvc add data/poems.txt`
output:

```bash
$ dvc add data/poems.txt
100% Adding...|█████████████████████████████|1/1 [00:00,  3.92file/s] 

To track the changes with git, run:

        git add 'data\poems.txt.dvc' 'data\.gitignore'

To enable auto staging, run:

        dvc config core.autostage true
```

let's take a look at:

`poems.txt.dvc`

```txt
outs:
- md5: 46648ad71a70dd101064231be171722c
  size: 107
  hash: md5
  path: poems.txt
```

as you can see it added a hash and some other information.

Also we not any longer tacking the `poems.txt`. See `.gitignore`. We track the dvc, hash file above!





Troubleshoot:

1) If you get this error, might want to add a version control like git (`git init`)

```bash
ERROR: failed to initiate DVC - C:\Users\AX-St\MyGIthub\POW_DVC is not tracked by any supported SCM tool (e.g. Git). Use `--no-scm` if you don't want to use any SCM or `--subdir` if initializing inside a subdirectory of a parent SCM repository.
```