# Typical Workflow 

1. Create a conda environment. `conda create --name {name} python={#}` 

2. Export the environment to a yaml file in `env-files`. 

```
conda activate {name}
conda env export --from-history > env-files/{name}
```

    a. This snippet can be used to update the env as you download more 
       dependencies. 

    b. `--from-history` tag ensure that the environment can be built across 
       different operating systems.

3. Dump raw data into `Data/raw`.

4. Start exploring in Notebooks. 

5. When a direction is clear, most code should be written in self contained 
   packages/modules in `scripts/`. 

6. For more complex tasks, tests should be written first to validate the 
   codes behavior. Use `pytest` to automatically run all tests in the repo. 
