# end-to-end-nlp

```bash
## Workflows
Update config.yaml
Update params.yaml
Update entity
Update the configuration manager in src config
update the conponents
update the pipeline
update the dvc.yaml
update the app.py
```

## Steps:

1. Git clone the repository and Define template of the project

```bash
touch template.py
python3 template.py
```

2. define setup.py scripts (**The setup.py** is a module used to build and distribute Python packages. It typically contains information about the package)

3. Create environment and install dependencies

```bash
conda create -n txt-env python=3.9 -y
conda activate txt-env
pip install -r requirements.txt
```

4. define logger (**The Logging** is a means of tracking events that happen when some software runs)

5. define utils (**The utils.py** makes it easy to execute common tasks in Python scripts)

6. run a notebook in google colab for experiment purpose and download it to "notebooks/" dir



7. ####################Data Ingestion##########################

Note: Data ingestion is the process of importing large, assorted data files from multiple sources into a single, cloud-based storage medium.

define config/config.yaml --> define constants/init.py --> and create 01_data_ingestion.ipynb and run it

define entity/init.py --> define /config/configuration.py --> define components/data_ingestion.py --> define pipeline --> and dvc.yaml --> finally run the dvc pipeline

8. ####################Data Validation##########################

Note: Data validation is the process of ensuring data has undergone data cleansing to confirm they have data quality, that is, that they are both correct and useful.

define config/config.yaml --> and create 02_data_validation.ipynb and run it

define entity/init.py --> define /config/configuration.py --> define components/data_validation.py --> define pipeline --> define dvc.yaml and run

9. ####################Data Transformation##########################

Note: Data transformation means taking data stored in one format and converting it to another

define config/config.yaml --> and create 03_data_transformation.ipynb and run it

define entity/init.py --> define /config/configuration.py --> define components/data_transformation.py --> define pipeline --> define and run dvc.yaml