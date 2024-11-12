class Univariate():
    def quanQual(dataset):
        quan=[]
        qual=[] 
        for columName in dataset.columns:
            
            print(columName)
            if(dataset[columName].dtype=='O'):
                
                print("qual")
                qual.append(columName)
            else:
                
                print("quan")
                quan.append(columName)
        return quan,qual


    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","RelativeFrequency","Cusum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().index
        freqTable["RelativeFrequency"]=(freqTable["Frequency"]/103)
        freqTable["Cusum"]=freqTable["RelativeFrequency"].cumsum()
       
        return freqTable
                
        
                
        
         
        
               

    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for column_name in quan:
            descriptive[column_name]["Mean"]=dataset[column_name].mean()
            descriptive[column_name]["Median"]=dataset[column_name].median()
            descriptive[column_name]["mode"]=dataset[column_name].mode()[0]
            descriptive[column_name]["Q1:25%"]=dataset.describe()[column_name]["25%"]
            descriptive[column_name]["Q2:50%"]=dataset.describe()[column_name]["50%"]
            descriptive[column_name]["Q3:75%"]=dataset.describe()[column_name]["75%"]
            descriptive[column_name]["Q4:100%"]=dataset.describe()[column_name]["max"]
            descriptive[column_name]["IQR"]=descriptive[column_name]["Q3:75%"]=descriptive[column_name]["Q1:25%"]
            descriptive[column_name]["1.5rule"]=1.5*descriptive[column_name]["IQR"]
            descriptive[column_name]["Lesser"]=descriptive[column_name]["Q1:25%"]-descriptive[column_name]["1.5rule"]
            descriptive[column_name]["Greater"]=descriptive[column_name]["Q3:75%"]+descriptive[column_name]["1.5rule"]
            descriptive[column_name]["Min"]=dataset[column_name].min()
            descriptive[column_name]["Max"]=dataset[column_name].max()
            descriptive[column_name]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[column_name]["skew"]=dataset[columnName].skew()
            descriptive[column_name]["var"]=dataset[columnName].var()
            descriptive[column_name]["std"]=dataset[columnName].std()
            
        return descriptive  
            
                
            
                                                                                                                                                                          
    def ReplaceOtlier():
        
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[colunName]["Lesser"]
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[colunName]["Greater"]
        return ReplaceOtlier
        
                                                                                                                                                                                                                                                                                                                               
    def OutlierColumnName():
        lesser=[]
        greater=[]
        for colunName in quan:
            if(descriptive[colunName]["Min"]<descriptive[colunName]["Lesser"]):
                lesser.append(colunName)
            if(descriptive[colunName]["Max"]>descriptive[colunName]["Greater"]):
                greater.append(colunName)
        return OutlierColumnName          
        
           
           
          
          
       
                    
                
                    
              
                  
          
            
                       
      

        