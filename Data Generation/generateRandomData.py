from random import seed
from random import random
import random
def generateRandomData(df, numberOfRowsToGenerate):
    seed()
    d = {}
    #df_random = pd.DataFrame()
    #GET ALL THE VALUES IN THE DATAFRAME, SAVE THEM TO A DICTIONARY. e.g., "Housing" (column name) -> [on campus, off campus] (possible values)
    for column in df: 
        # Select column contents by column 
        # name using [] operator 
        columnSeriesObj = df[column] 
        d[column] = columnSeriesObj.unique()
    #CREATE THE DATAFRAME
    df_random = pd.DataFrame(columns = d.keys())
    #CREATE A ROW
    for x in range(numberOfRowsToGenerate):
        NewRow = []
        for x in d.keys():
            maxAddress = d.get(x).size-1
            minAddress = 0
            address = random.randint(minAddress,maxAddress)
            randomVal = d.get(x)[address]
            NewRow.append(randomVal)    
        #print(NewRow)
        #Add the row
        df_random.loc[-1] = NewRow
        # shifting index
        df_random.index = df_random.index + 1 
    return df_random
