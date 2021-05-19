# licenses-datamining
Script that:
- Download repositories from csv
- Iterates over the repositories by running LicenseFinder
- Dump the result of LicenseFinder execution in a file

This experiment can be replicated to projects that your programming language is supported with LicenseFinder.
[List of supported project types](https://github.com/pivotal/LicenseFinder#supported-project-types)
## Requirements
- [Python3](https://www.python.org/downloads/)
- [LicenseFinder (Execution with Docker)](https://github.com/pivotal/LicenseFinder)
- Dataset `.csv` in `src/repositories.csv`. [Recommended dataset](https://zenodo.org/record/804474#.YKMBDHVKiV4) or another with the same structure.

## Experiment replication

### Clone the repository:
```sh
$ git clone https://github.com/dennisurtubia/licenses-datamining.git
```
### Script execution
```sh
$ cd licenses-datamining
$ sudo python3 src/execute.py NUMBER_OF_PROCESS # NUMBER_OF_PROCESS 0 or 1
```

## Expreriment output
Example for [Cookies](https://github.com/ScottHamper/Cookies) project execution:
```json
{
    "Cookies": {
        "dependencies": [
            {
                "name": "cookies-js",
                "version": "1.2.4-pre",
                "licenses": ["Public Domain"]
            }
        ]
    }
}
```