# Get Started (Python)
  
### Step 0: Orient yourself to Domino 
  
### Step 1: Create a project
  
### Step 2: Configure your project  
Every project has its own settings.  
Important options when configuring a new project:
* Hardware Tier  
compute resources (CPU/GPU)
* Environment
Configure the **software, packages, libaries, and drivers** that you need.
* Collaborators
 invite a colleague to be a Contributor
 
### Step 3: Start a workspace
interactive sessions (interact with code notebooks like Jupyter and RStudio)  
hosted by **executor** (machine)  -  container
  
  
### Step 4: Get your files and data
* copy
Eg:  jupyter  
/mnt (root)
terminal : curl -o data.csv "https://www..."  
Full Sync  
* query

### Step 5: Develop your model
goal: execute code, see outputs, and make iterative improvements
* Load and explore the dataset
* Train a model  
[a package that is new and not installed in the environment]  
pip install
* Export the model  
```
import pickle   
with open("model.pkl", "wb") as f:  
      pickle.dump(m, f)  
```

### Step 6: Clean up
avoid spending unnecessary compute resources  
* from inside the workspace
Jupyter notebook - menu bar - Stop
* from the Workspaces page  
Workspaces page - stop

### Step 7: Deploy your model
* Scheduled reports  
[each day we receive new data on power usage. To make sure our predictions are accurate as possible, we can schedule our notebook to re-train our model with the latest data and update the visualization accordingly]  
```
import datetime
today = datetime.datetime.today().strftime('%Y-%m-%d')
one_month = (datetime.datetime.today() - datetime.timedelta(30)).strftime('%Y-%m-%d')
!curl -o data.csv "..."
```
Scheduled Jobs page - file name - daily run time - send the result  

* Launchers  
Launchers are simple web forms that allow users to run templatized scripts.  
useful if your script has command line arguments  
menu bar - View/Cell Toolbar/Tags  - "parameters"  
creat default parameters  
```
start_date_str = 'Tue Oct 08 2019 00:00:00 GMT-0700 (Pacific Daylight Time)'
fuel_type = 'CCGT'
```

change data format (Launcher parameters - notebook parameter)
```
import datetime
today = datetime.datetime.today().strftime('%Y-%m-%d')
start_date = datetime.datetime.strptime(start_date_str.split(' (')[0], '%a %b %d %Y 00:00:00 GMT%z').strftime('%Y-%m-%d')
```

```
!curl -o data.csv "..."
```

In the cell that you define df_for_prophet, replace 'CCGT' with fuel_type  
  
Create a new file called forecast_launcher.sh  #shell file  
```
papermill Forecast_Power_Generation_for_Launcher.ipynb forecast.ipynb -p start_date "$1" -p fuel_type $
```
- Papermill is a tool to inject configuration into a notebook, launch it and collect the results.  
- notebook must be prepared accordingly, as Papermill executes notebooks in-order.  
- papermill <input ipynb file> <output ipynb file> -p <parameter name> <parameter value>  
- **shell** $1～$n: parameter value. the first parameter/ second parameter  
  
    
configure the Launcher - Launcher -  New Launcher  
command to run - forecast_launcher.sh ${start_date} ${fuel_type}  


* Web applications
* Model APIs

Training and Feature Overviews
