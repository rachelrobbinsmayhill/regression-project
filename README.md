Regression Project - Zillow -
Codeup - Innis Cohort - March 2022
 
===
 
Table of Contents
---
 
* I. [Project Overview](#i-project-overview)<br>
[1. Goals](#1-goal)<br>
[2. Description](#2-description)<br>
[3. Initial Questions](#3initial-questions)<br>
[4. Formulating Hypotheses](#4-formulating-hypotheses)<br>
[5. Deliverables](#5-deliverables)<br>
* II. [Project Data Context](#ii-project-data-context)<br>
[1. Data Dictionary](#1-data-dictionary)<br>
* III. [Project Plan - Data Science Pipeline](#iii-project-plan---using-the-data-science-pipeline)<br>
[1. Project Planning](#1-plan)<br>
[2. Data Acquisition](#2-acquire)<br>
[3. Data Preparation](#3-prepare)<br>
[4. Data Exploration](#4explore)<br>
[5. Modeling & Evaluation](#5-model--evaluate)<br>
[6. Product Delivery](#6-delivery)<br>
* IV. [Project Modules](#iv-project-modules)<br>
* V. [Project Reproduction](#v-project-reproduction)<br>
 
 
 
## I. PROJECT OVERVIEW
 
 
#### 1.  GOAL:

 
 
#### 2. DESCRIPTION:

 
 
#### 3.INITIAL QUESTIONS:

##### Data-Focused Questions

 
##### Overall Project-Focused Questions

 

#### 4. FORMULATING HYPOTHESES

 
#### 5. DELIVERABLES:
- [x] README file - provides an overview of the project and steps for project reproduction. 
- [x] Draft Jupyter Notebooks - provide all steps taken to produce the project.
- [x] Python Module File - provides reproducible code for acquiring,  preparing, exploring, & testing the data.
- [x] acquire.py - used to acquire data
- [x] prepare.py - used to prepare data
- [x] Report Jupyter Notebook - provides final presentation-ready assessment and recommendations.
- [x] 5 minute presentation to stakeholders
 
 
## II. PROJECT DATA CONTEXT
 
#### 1. DATA DICTIONARY:
The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:
 
 
Feature	Data Type	Used In	Description
airconditioningtypeid			 Type of cooling system present in the home (if any)
architecturalstyletypeid			 Architectural style of the home (i.e. ranch, colonial, split-level, etc…)
basementsqft			 Finished living area below or partially below ground level
bathroomcnt	float64	Workbook	 Number of bathrooms in home including fractional bathrooms
bedroomcnt	float64		 Number of bedrooms in home 
buildingqualitytypeid			 Overall assessment of condition of the building from best (lowest) to worst (highest)
buildingclasstypeid			The building framing type (steel frame, wood frame, concrete/brick) 
threequarterbathnbr			 Number of 3/4 bathrooms in house (shower + sink + toilet)
finishedfloor1squarefeet			 Size of the finished living area on the first (entry) floor of the home
square_feet	float64	Workbook	 Calculated total finished living area of the home 
geo_code	object	Workbook	 Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS_county_code for more details
fireplaceflag			 Is a fireplace present in this home 
fullbathcnt			 Number of full bathrooms (sink, shower + bathtub, and toilet) present in home
hashottuborspa			 Does the home have a hot tub or spa
heatingorsystemtypeid			 Type of home heating system
latitude			 Latitude of the middle of the parcel multiplied by 10e6
longitude			 Longitude of the middle of the parcel multiplied by 10e6
lotsizesquarefeet			 Area of the lot in square feet
numberofstories			 Number of stories or levels the home has
parcelid		SQL Join	 Unique identifier for parcels (lots) 
poolcnt			 Number of pools on the lot (if any)
propertylandusetypeid		SQL Join	 Type of land use the property is zoned for
propertyzoningdesc			 Description of the allowed land uses (zoning) for that property
regionidcounty			County in which the property is located
regionidcity			 City in which the property is located (if any)
regionidzip			 Zip code in which the property is located
regionidneighborhood			Neighborhood in which the property is located
roomcnt			 Total number of rooms in the principal residence
storytypeid			 Type of floors in a multi-story house (i.e. basement and main level, split-level, attic, etc.).  See tab for details.
typeconstructiontypeid			 What type of construction material was used to construct the home
yardbuildingsqft17			Patio in  yard
yardbuildingsqft26			Storage shed/building in yard
year_built	int64	Workbook	 The Year the principal residence was built 

## III. PROJECT PLAN - USING THE DATA SCIENCE PIPELINE:
The following outlines the process taken through the Data Science Pipeline to complete this project. 
 
Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver
 
#### 1. PLAN
- [x] Review project expectations
- [x] Draft project goal to include measures of success
- [x] Create questions related to the project
- [x] Create questions related to the data
- [x] Create a plan for completing the project using the data science pipeline
- [x] Create a data dictionary to define variables and data context
- [x] Draft starting hypothesis
 
#### 2. ACQUIRE
- [x]  Create .gitignore
- [x]  Create env file with log-in credentials
- [x]  Store env file in .gitignore to ensure security of sensitive data
- [x]  Create acquire.py module
- [x]  Store functions needed to acquire the Zillow dataset from mySQL
- [x]  Ensure all imports needed to run the functions are inside the acquire.py document
- [x]  Using Jupyter Notebook
- [x]  Run all required imports
- [x]  Import functions from aquire.py module
- [x]  Summarize dataset using methods and document observations
 
#### 3. PREPARE
Using Python Scripting Program (VS Code)
- [x] Create prepare.py module
- [x] Store functions needed to prepare the Zillow data such as:
   - [x] Split Function: to split data into train, validate, and test
   - [x] Cleaning Function: to clean data for exploration
   - [x] Encoding Function: to create numeric columns for object column
   - [x] Feature Engineering Function: to create new features
- [x] Ensure all imports needed to run the functions are inside the prepare.py document
Using Jupyter Notebook
- [x] Import functions from prepare.py module
- [x] Summarize dataset using methods and document observations
- [x] Clean data
- [x] Features need to be turned into numbers
- [x] Categorical features or discrete features need to be numbers that represent those categories
- [x] Continuous features may need to be standardized to compare like datatypes
- [x] Address missing values, data errors, unnecessary data, renaming
- [x] Split data into train, validate, and test samples
 
#### 4.EXPLORE
Using Jupyter Notebook:
- [x] Answer key questions about hypotheses and find drivers of churn
  - Run at least two statistical tests
  - Document findings
- [x] Create visualizations with intent to discover variable relationships
  - Identify variables related _______________
  - Identify any potential data integrity issues
- [x] Summarize conclusions, provide clear answers, and summarize takeaways
  - Explain plan of action as deduced from work to this point
 
#### 5. MODEL & EVALUATE
Using Jupyter Notebook:
- [x] Establish baseline accuracy
- [x] Train and fit multiple (3+) models with varying algorithms and/or hyperparameters
- [x] Compare evaluation metrics across models
- [x] Remove unnecessary features
- [x] Evaluate best performing models using validate set
- [x] Choose best performing validation model for use on test set
- [x] Test final model on out-of-sample testing dataset
- [x] Summarize performance
- [x] Interpret and document findings
 
#### 6. DELIVERY
- [x] Prepare five minute presentation using Jupyter Notebook
- [x] Include introduction of project and goals
- [x] Provide executive summary of findings, key takeaways, and recommendations
- [x] Create walk through of analysis 
  - Visualize relationships
  - Document takeaways
  - Explicitly define questions asked during initial analysis
- [x] Provide final takeaways, recommend course of action, and next steps
- [x] Be prepared to answer questions following presentation

 
 
## IV. PROJECT MODULES:
- [x] Python Module Files - provide reproducible code for acquiring,  preparing, exploring, & testing the data.
   - [x] acquire.py - used to acquire data
   - [x] prepare.py - used to prepare data
 
  
## V. PROJECT REPRODUCTION:
### Steps to Reproduce
 
- [x] You will need an env.py file that contains the hostname, username, and password of the mySQL database that contains the telco_churn database
- [x] Store that env file locally in the repository
- [x] Make .gitignore and confirm .gitignore is hiding your env.py file
- [x] Clone my repo (including the acquire.py and prepare.py)
- [x] Import python libraries:  pandas, matplotlib, seaborn, numpy, and sklearn
- [x] Follow steps as outlined in the README.md. and Churn_Work.ipynb
- [x] Run Zillow_Report.ipynb to view the final product