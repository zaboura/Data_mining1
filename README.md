# Data mining project 1:

This task summarises by an observation over the results of survey done in  
2016 by INSEE (Institute national de statistiques et des études économique). This examination provided vast information about individuals living in France. 

Data localized to different regions and departments of EPCI "Les établissements publics de coopération intercommunale", generally describes the characteristics of each person enumerated. Variables available with detailed modalities, including restricted variables (nationality, country of birth, seniority of arrival in France).
For this project we are working with gathered information for Grand Est state. the original dataset made by more than 90 attributes for 1,474,559 queries (transactions). However we are working on some candidate attributes after basic research we done for entire dataset.

We were also interested to interpret our data in such a  away that we can discover meaningful information, as a role of journalist offered by the professor for this work.

The Selected features for this anaysis are  ```AGER20, ANEMR, SFM, NPERR, VOIT, MODV, CS1, ILTUU, EMPL, MOCO```.
## Description of the features:

__EMPL__ :Condition of employment 

* 11 - In apprenticeship or professionalization contract
* 12 - Placed by a temporary employment agency
* 13 - Supported jobs (single integration contract, employment initiative, support in employment, future, etc.)
* 14 - Paid interns in a company
* 15 - Other jobs of limited duration, CDD, short contract, seasonal, temporary, etc.
* 16 - Jobs without term limit, CDI, civil servant
* 21 - Non-salaried: Self-employed
* 22 - Non-salaried: Employers
* 23 - Non-salaried: Family helpers
* ZZ - Not applicable


----------------------------------------------------------------------------------

__AGER20__: Age in completed years (age at last birthday) in 13 age groups, detailed around 20 years

* 02 - Two years and under
* 05 - 3 to 5 years old
* 10 - 6 to 10 years old
* 14 - 11 to 14 years old
* 17 - 15 to 17 years old
* 19 - 18 to 19 years old
* 24 - 20 to 24 years old
* 29 - 25 to 29 years old
* 39 - 30 to 39 years old
* 54 - 40 to 54 years old
* 64 - 55 to 64 years old
* 79 - 65 to 79 years old
* 80 - 80 years or over


----------------------------------------------------------------------------------
__ANEMR__: Age of moving into the accommodation (grouped together)

List of codes
* 00 - Less than 2 years
* 01 - 2 to 4 years old
* 02 - From 5 to 9 years old
* 03 - 10 to 19 years old
* 04 - 20 to 29 years old
* 05 - From 30 to 39 years old
* 06 - 40 to 49 years old
* 07 - 50 to 59 years old
* 08 - 60 to 69 years old
* 09 - 70 years or older
* 99 - Unoccupied ordinary dwelling
* ZZ - Excluding ordinary accommodation

----------------------------------------------------------------------------------

__SFM__: Family structure of the household

List of codes
* 11 - Person living alone: ​​man
* 12 - Person living alone: ​​woman
* 21 - A main single-parent family without single parent: man with child (ren)
* 22 - A main single-parent family without single parents: woman with child (ren)
* 30 - Main family a couple without single without children
* 31 - Main family a couple without single with 1 child
* 32 - Main family a couple without single with 2 children
* 33 - Main family a couple without single with 3 children
* 34 - Main family a couple without single with 4 or more children
* 40 - A main single-parent family with single (s)
* 51 - Main family a couple without children with single (s) all ascendant (s) or descendant (s)
* 52 - Main family a couple without children with other isolated (s)
* 53 - Main family a couple with child (ren) with single (s) all ascendant (s) or
descendant (s)
* 54 - Main family a couple with child (ren) with other single (ren)
* 61 - Two families with or without single (s): two couples with or without child (ren)
* 62 - Two families with or without single (s): other cases
* 70 - Other household without family
* ZZ - Excluding ordinary accommodation

----------------------------------------------------------------------------------

__NPERR__: Number of people in the household (grouped)

List of codes
* 1 - One person
* 2 - 2 people
* 3 - 3 people
* 4 - 4 people
* 5 - 5 people
* 6 - 6 or more people
* Z - Excluding ordinary accommodation


---------------------------------------------------------------------------------

__VOIT__: Number of cars in the household

List of codes
* 0 - No car
* 1 - One car
* 2 - Two cars
* 3 - Three or more cars
* X - Unoccupied ordinary dwelling
* Z - Excluding ordinary accommodation

---------------------------------------------------------------------------------

__MODV__: Way of life

List of codes
* 11 - Children of a couple
* 12 - Children of a single-parent family
* 20 - Unattached individuals under 40
* 31 - Members under 40 of a childless couple
* 32 - Members of a couple with children
* 33 - Parents of a single-parent family
* 40 - Members aged 40 or over in a childless couple
* 50 - Unattached individuals aged 40 or over
* 60 - Persons living outside their family in a household of several persons
* 70 - People living outside the household

---------------------------------------------------------------------------------

__CS1__: Socio-professional category in 8 positions

List of codes
* 1 - Farmer operators
* 2 - Craftsmen, traders and business leaders
* 3 - Managers and higher intellectual professions
* 4 - Intermediate Professions
* 5 - Employees
* 6 - Workers
* 7 - Retirees
* 8 - Other people without professional activity

---------------------------------------------------------------------------------

__ILTUU__: Urban workplace indicator

List of codes
* 1 - Resides in a rural municipality and works in the same municipality
* 2 - Live in a rural municipality and work outside the municipality
* 3 - Resides in an urban municipality and works in the same municipality
* 4 - Resides in an urban municipality and works in another municipality of the same unit urban
* 5 - Resides in an urban municipality and works outside the urban unit
* Z - Not applicable

---------------------------------------------------------------------------------

__MOCO__: Mode of cohabitation

List of codes
* 11 - Children of a couple
* 12 - Children of a single-parent family
* 21 - Adults of a couple without children
* 22 - Adults of a couple with child (ren)
* 23 - Adults in a single-parent family
* 31 - Non-family in a household of several people
* 32 - People living alone
* 40 - People living outside the household
 
## To run the code

To encode the files run the following commad line:

    python Encode_data_forSPMF.py.py ../Data/GrantEast  ../Results/file_name.txt
    
To decode the output of SPMF tool, run the following command line:

     python DecoderforSPMF.py path_to_file path_of_output_file.txt

We took as supports 10%, 20%, and 50% for both algorithms: Apriori(Ap) and Apriori Association Rules (AAR).

The name of the file in Results folder indicate which algorithm and support used to generate it.
## Architecture of depository:


Data_minig1/

           Code/
                DecoderforSPMF.py 
                Encode_data_forSPMF.py
          
           Data/
                GrandEst
           
           Files_pdf/
                SignificationDesVariables.pdf
                TP-project.pdf
           
           Results/
                encoded_files.txt
                decoded_files.txt
                invdico.dbm 
           
           Tools/
                spmf.jar


