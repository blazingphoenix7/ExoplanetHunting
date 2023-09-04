from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import pandas as pd
import pickle
import sklearn

# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload(request):
    return render(request,'upload.html')

def predictExoplanet(request):
    exoplanet_list=[]
    show = True;
    fileObj=request.FILES['filePath']
    if not fileObj.name.endswith('csv'):
        messages.info(request,'Wrong format')
        return render(request, 'upload.html')
    else:
        csv = pd.read_csv(fileObj)
        print(csv.head())
        # computing number of rows
        rows = len(csv.axes[0])
    
        # computing number of columns
        cols = len(csv.axes[1])
        #loading the model
        model = pickle.load(open('./models/exoplanet.pkl','rb'))
        for i in range(12):
            data = csv.iloc[i]
            #data = data.drop(["LABEL"])
            #print(data.shape)
            #label = csv.iloc[1]
            #label = label["LABEL"]
            data = data.values.reshape(1,3197)
            #print(data.shape)
            result = model.predict(data)
            print(result)
            if result[0]==0:
                exoplanet_list.append("Doesn't contain an Exoplanet")
            else:
                exoplanet_list.append("Contains an Exoplanet")
        print(exoplanet_list)
        #data=csv.iloc[1]    #rowise data
        #print(data.shape)
        #data=data.values.reshape(1,3197)
        #print(data.shape)
        #result=model.predict(data)
        #print(result)
        fs=FileSystemStorage()
        filePathName=fs.save(fileObj.name, fileObj)
        filePathName=fs.url(filePathName)
        print(filePathName)
        context={'filePathName':filePathName,'show':show,'exoplanet_list':exoplanet_list}
        return render(request, 'upload.html', context)
     