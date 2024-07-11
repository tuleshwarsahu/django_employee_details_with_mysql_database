from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import collections
import mysql.connector
from django.db import connection

from django.utils.datastructures import MultiValueDictKeyError

from django.core import serializers
from django.urls import reverse
# Create your views here.



def adddata(req):
	
	template = loader.get_template('adddetail.html')
	resData={'Message':''}
	return HttpResponse(template.render(resData, req))

def updaterec(req):
	print(req.GET['id'])
	template = loader.get_template('updatedata.html')
	resData={'ID':req.GET['id'],"name":req.GET['name'],"phone":req.GET['phone'],"address":req.GET['address'],"salary":req.GET['salary']}
	return HttpResponse(template.render(resData,req))

def saveData(req):
	connection=mysql.connector.connect(host="localhost",user="root",password="",database="test")
	print(req.POST['id'])
	print(req.POST['name'])
	print(req.POST['phone'])
	print(req.POST['address'])
	print(req.POST['salary'])
	mycursor = connection.cursor()
	sql="insert into employees (EmpID,Emp_Name,phone_no,address,salary) values(%s,%s,%s,%s,%s)"
	val=(req.POST['id'],req.POST['name'],req.POST['phone'],req.POST['address'],req.POST['salary'])
	mycursor.execute(sql,val)
	connection.commit()
	if mycursor.rowcount>0:
		resData={'Message':'Record added'}
	else:
		resData={'Message ':'Record not added'}
	template = loader.get_template('adddetail.html')
	return HttpResponse(template.render(resData, req))

def showData(req):
	connection=mysql.connector.connect(host="localhost",user="root",password="",database="test")
	cursor=connection.cursor()
	cursor.execute("select * from employees")
	result = cursor.fetchall()
	data=[]
	for x in result:
		d = collections.OrderedDict()
		d['id'] = x[0]
		d['name'] = x[1]
		d['phone'] = x[2]
		d['address'] = x[3]
		d['salary'] = x[4]
		data.append(d)
		print(d)
	
	resData={'users':data}
	template = loader.get_template('listUsers.html')
	return HttpResponse(template.render(resData, req))


def updatedone(req):
	connection=mysql.connector.connect(host="localhost",user="root",password="",database="test")
	print(req.POST['id'])
	print(req.POST['name'])
	print(req.POST['phone'])
	print(req.POST['address'])
	print(req.POST['salary'])
	mycursor = connection.cursor()
	sql="update employees set Emp_Name=%s,phone_no=%s,address=%s,salary=%s where EmpID=%s"
	val=(req.POST['name'],req.POST['phone'],req.POST['address'],req.POST['salary'],req.POST['id'])
	mycursor.execute(sql,val)
	connection.commit()
	mycursor.execute("select * from employees")
	result=mycursor.fetchall()
	data=[]
	for x in result:
		d = collections.OrderedDict()
		d['id'] = x[0]
		d['name'] = x[1]
		d['phone'] = x[2]
		d['address'] = x[3]
		d['salary'] = x[4]
		data.append(d)
		print(d)
	
	resData={'users':data}
	template = loader.get_template('listUsers.html')
	return HttpResponse(template.render(resData,req))

def deletefile(req):
	print(req.GET['id'])
	template = loader.get_template('delete.html')
	resData={'ID':req.GET['id'],"name":req.GET['name'],"phone":req.GET['phone'],"address":req.GET['address'],"salary":req.GET['salary']}
	return HttpResponse(template.render(resData,req))

def deletedata(req):
	connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "test")
	#print(req.GET['id']) 
	print(req.POST['name'])
	print(req.POST['phone'])
	print(req.POST['address'])
	print(req.POST['salary'])
	mycursor = connection.cursor()
	
	sql="delete from emp  where EmpID ="+req.POST['id']
 
	mycursor.execute(sql)

	connection.commit()
	mycursor.execute("select * from emp")

	result = mycursor.fetchall()

	data=[]

	for x in result:

		d = collections.OrderedDict()
		d['id'] = x[0]
		d['name'] = x[1]
		d['phone'] = x[2]
		d['address'] = x[3]
		d['salary'] = x[4]
		data.append(d)
	print(d)

	resData={'users':data}
	template = loader.get_template('listUsers.html')
	return HttpResponse(template.render(resData,req))


     




