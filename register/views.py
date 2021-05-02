from django.shortcuts import render
import joblib
import pandas as pd

# Create your views here.
reloadmodel=joblib.load('./models/LR_MODEL_FOR_SALES_PRICE.pkl')
def index(resquest):
	return render(resquest,'register.html',
		{'link':'http://127.0.0.1:8000/','a':'http://127.0.0.1:8000/register/','b':'http://127.0.0.1:8000/help/'})


def predict(request):
	if (request.method == 'POST'):
		temp={}
		temp['INT_SQFT']=request.POST.get('INT_SQFT')
		temp['DIST_MAINROAD']=request.POST.get('DIST_MAINROAD')
		temp['COMMIS']=request.POST.get('COMMIS')
		temp['AREA']=request.POST.get('AREA')
		temp['N_BEDROOM']=request.POST.get('N_BEDROOM')
		temp['N_BATHROOM']=request.POST.get('N_BATHROOM')
		temp['N_ROOM']=request.POST.get('N_ROOM')
		temp['SALE_COND']=request.POST.get('SALE_COND')
		temp['PARK_FACIL']=request.POST.get('PARK_FACIL')
		temp['BUILDTYPE']=request.POST.get('BUILDTYPE')
		temp['STREET']=request.POST.get('STREET')
		print(temp)
	obj_val=[temp['AREA'],temp['N_BEDROOM'],temp['N_BATHROOM'],temp['N_ROOM'],temp['SALE_COND']
	,temp['PARK_FACIL'],temp['BUILDTYPE'],temp['STREET']]
	list1=['AREA_1','AREA_2', 'AREA_3', 'AREA_4', 'AREA_5', 'AREA_6', 'AREA_7',
       'N_BEDROOM_1', 'N_BEDROOM_2', 'N_BEDROOM_3', 'N_BEDROOM_4',
       'N_BATHROOM_1', 'N_BATHROOM_2', 'N_ROOM_2', 'N_ROOM_3', 'N_ROOM_4',
       'N_ROOM_5', 'N_ROOM_6', 'SALE_COND_1', 'SALE_COND_2', 'SALE_COND_3',
       'SALE_COND_4', 'SALE_COND_5', 'PARK_FACIL_0', 'PARK_FACIL_1',
       'BUILDTYPE_1', 'BUILDTYPE_2', 'BUILDTYPE_3', 'STREET_1', 'STREET_2',
       'STREET_3']
	list2=['INT_SQFT', 'DIST_MAINROAD', 'COMMIS']
	temp_new={}
	for i in list2:
		temp_new[i]=temp[i]
	for i in list1:
		if(i in obj_val):
			temp_new[i]=1
		else:
			temp_new[i]=0
	
	print(temp_new)
	x1=pd.DataFrame({'a':temp_new}).transpose()
	price=reloadmodel.predict(x1)[0]

	tem=price
	x1.insert(34,'SALES_PRICE',[tem],True)
	used=pd.read_csv(r'./models/used.csv')
	used.append(x1,ignore_index=True, verify_integrity=True).to_csv(r'./models/used.csv')
	used=pd.read_csv(r'./models/used.csv')
	used.drop(["Unnamed: 0"],axis=1,inplace=True)

	context={'price':price,'link':'http://127.0.0.1:8000/','a':'http://127.0.0.1:8000/register/',
	'b':'http://127.0.0.1:8000/help/'}
	return render(request,'result.html',context)
	
	