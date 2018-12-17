# create_artifacts
This script will generate 1000 user stories and defects in the specified Agile Central project.  A percentage of the created artifacts will also include a random number of tasks.

### Installation:
`pip install requests`

`pip install pyral`

`pip install lorem`

### Usage:
`python create_artifacts.py --server=<hostname> --user=<login ID> --password=<password> --workspace="<workspace>" --project="<project>"`


### Output:
```
Defect created, ObjectID: 3005344  FormattedID: DE22603
HierarchicalRequirement created, ObjectID: 3005408  FormattedID: S91
Task created, ObjectID: 3005464  FormattedID: TA76
Task created, ObjectID: 3005519  FormattedID: TA77
Task created, ObjectID: 3005560  FormattedID: TA78
Defect created, ObjectID: 3005601  FormattedID: DE22604
```
