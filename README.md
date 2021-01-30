# Data mining project 1:

## To run the code

Go to the code diractory and run the following commad lines:

    python file_name.py path_to_data path_to_store_output_file (the last argument is optional)
    python file_name.py ../Data/GrantEast  ../Results/file_name
    
    
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
                encoded_file.txt
                invdico.dbm 
           
           Tools/
                spmf.jar

