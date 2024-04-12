# MLProjectTemplate
A reusable template with MLOPs frameworks for your Data Science project

## Setting Up the Project using this template:
1. Click on `Use this template` -> `create a new repository`
2. Put your repository name and description -> `create repository`
3. Clone the repository to your local machine 
4. Rename the project folder `(src/YourProjectName)` to your project name
5. Update requirements.txt with the required libraries 
6. Create a virtual environment using setup.sh:
    ```
    bash setup.sh 
    ```
7. Activate the virtual environment (optional, if not done in step 6):
    ```
    source activate ./venv
    ``` 
------------------------------------------------------------------------------------------------------------------------
## Workflow:
1. Update config: `config/config.yaml`
2. Update raw/processed data schema: `raw_schema.yaml/processed_schema.yaml` (if needed)
3. Update model parameters: `params.yaml` (if needed)
4. Update the entity: `src/RuralCreditPredictor/entity/config_entity.py`
5. Update the configuration manager: `src/RuralCreditPredictor/config/configuration.py`
6. Update the components: `src/RuralCreditPredictor/components`
7. Update the pipeline: `src/RuralCreditPredictor/pipeline`
8. Update entrypoint: `main.py`
9. Update application: `app.py`

------------------------------------------------------------------------------------------------------------------------
