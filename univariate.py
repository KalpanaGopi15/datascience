class univariate():
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for columnname in dataset.columns:
            if(dataset[columnname].dtype=='O'):
                qual.append(columnname)
            else:
                quan.append(columnname)
        return quan,qual