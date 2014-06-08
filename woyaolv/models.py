from django.db import models
from django.contrib.auth.models import User,Group

class user_traveler(models.Model):
	#table of traveler with personal information in detail 
	user=models.ForeignKey(User)
	birthday=models.DateField(blank=True)#birthday of the traveler(optional)
	#first_name=models.CharField(max_length=30)
	#last_name=models.CharField(max_length=30)
	photo=models.ImageField(upload_to='portrait_traveler',blank=True, null=True,)#photo of the traveler, better be real
	sex=models.CharField(max_length=30)#sex of the traveler(optional)
	phone=models.CharField(max_length=30)#phont number of the traveler
	status=models.CharField(max_length=30)#student, programmer, doctor, soldier, teacher...
	introduce=models.TextField(blank=True)#traveler's self introduction
	score=models.PositiveIntegerField()#for future use, traveler rating function
	smoke=models.PositiveIntegerField(blank=True)#
	drink=models.PositiveIntegerField(blank=True)#
	def __unicode__(self):
		return u'%s%s %s' % (self.user.last_name,self.user.first_name,self.user.username)
	class Meta:
		ordering = ['score']

class user_driver(models.Model):
	#table of driver with personal information in detail
	user=models.ForeignKey(User)
	birthday=models.DateField()#birthday of the driver
	#first_name=models.CharField(max_length=30)
	#last_name=models.CharField(max_length=30)
	photo=models.ImageField(upload_to='portrait_driver')#photo of the driver, better be real(optional)
	sex=models.CharField(max_length=30)
	phone=models.CharField(max_length=30)
	experience=models.PositiveIntegerField()#how many years of experience in driving and in guiding
	introduce=models.TextField()#driver self introduction(optional)
	score=models.PositiveIntegerField()#for future use, driver rating function
	def __unicode__(self):
		return u'%s%s %s' % (self.user.last_name,self.user.first_name,self.user.username)
	class Meta:
		ordering = ['score']

class planfix(models.Model):
	#table of recommended plans
	name=models.CharField(max_length=30)#name of the plan
	introduce=models.TextField()#travel plan introduction(optional)
	places=models.CharField(max_length=100)#travel destinations
	region=models.CharField(max_length=50)
	duration=models.PositiveSmallIntegerField()
	price=models.CharField(max_length=50)#rule of price for the plan
	season_recommended=models.CharField(max_length=50)#travel tips in season
	Accommodation=models.CharField(max_length=50)#hotel..
	remark=models.CharField(max_length=50)#more tips
	photo=models.ImageField(upload_to='portrait_planfix')#a portrait photo of the plan
	score=models.PositiveIntegerField()#for future use, travel plan rating function
	class Meta:
		ordering = ['score']
	def __unicode__(self):
		return u'%s' % (self.name)


class planfix_pictures(models.Model):
	planfix=models.ForeignKey(planfix)
	picture=models.ImageField(upload_to='planfix_pictures')	

class travel_propose(models.Model):
#a travel_propose can be declaired to the public only 1 month in advance of the start_date, and have to be valided 1 week before the start_date
	user_traveler=models.ForeignKey(user_traveler)#the treveler id who declaire the propose
	user_driver=models.ForeignKey(user_driver,blank=True,null=True,default = None)#the id of driver chosen by admin
	planfix=models.ForeignKey(planfix,blank=True)#for people chose to use the recommended travel plan(optional)
	phone=models.CharField(max_length=30)
	num_want=models.PositiveSmallIntegerField()#preference in number of travelers in total 
	num_now=models.PositiveSmallIntegerField()#number of travelers fixed
	start_date=models.DateField()#travel start date(1 month advanced)
	end_date=models.DateField()#travel end date
	region=models.CharField(max_length=30)
	places=models.TextField(blank=True)#travel destinations
	plan=models.TextField(blank=True)#for people make his/her own travel plan(optional)
	state=models.CharField(max_length=30)#waiting/valide/finised/closed
	people_with=models.CharField(max_length=200,blank=True)#++people with me...
	datetime_create=models.DateTimeField()
	def __unicode__(self):
		return u'%s,  %s, from %s to %s, proposed by "%s" at %s' % (self.region,self.end_date-self.start_date,self.end_date,self.start_date,self.user_traveler,self.datetime_create)


class travel_propose_traveler(models.Model):
	travel_propose=models.ForeignKey(travel_propose)
	traveler=models.ForeignKey(user_traveler)    #user id of people join the trip	
	def __unicode__(self):
		return u'"%s" join:  %s' % (self.traveler,self.travel_propose)


class from_airport(models.Model):
#table for storing the apply of pick up from airport
	user_traveler=models.ForeignKey(user_traveler)#id of traveler
	user_driver=models.ForeignKey(user_driver,blank=True,null=True,default = None)#driver chosen by the admin for this mission
	phone=models.CharField(max_length=30)
	num_Luggage=models.PositiveSmallIntegerField()#number of luggages
	num_people=models.PositiveSmallIntegerField()#mumber of people
	datetime=models.DateTimeField()#pick up date and time in detail -24h
	airport=models.CharField(max_length=50)#airport name
	flight_num=models.CharField(max_length=30)#flight number
	to_add=models.CharField(max_length=50)#address to go
	datetime_create=models.DateTimeField()
	def __unicode__(self):
		return u'"%s %s"  %s  %s  %s  "%s"' % ( self.user_traveler,self.phone,self.airport,self.flight_num,self.datetime,self.to_add)

class to_airport(models.Model):	
#table for storing apply of going to airport	
	user_traveler=models.ForeignKey(user_traveler)#id of traveler
	user_driver=models.ForeignKey(user_driver,blank=True,null=True,default = None)#driver chose by the admin for this mission
	phone=models.CharField(max_length=30)
	num_Luggage=models.PositiveSmallIntegerField()#number of luggages
	num_people=models.PositiveSmallIntegerField()#number of people
	datetime=models.DateTimeField()#date and time in detail -24
	airport=models.CharField(max_length=50)#airport name
	flight_num=models.CharField(max_length=30)#flight number
	from_add=models.CharField(max_length=50)#pick up address
	datetime_create=models.DateTimeField()
	def __unicode__(self):
		return u'"%s %s"  %s  %s  %s  "%s"' % ( self.user_traveler,self.phone,self.airport,self.flight_num,self.datetime,self.from_add)

class user_driver_comments(models.Model):
#comments on drivers
	user_driver=models.ForeignKey(user_driver)
	user_traveler=models.ForeignKey(user_traveler)
	grade=models.PositiveSmallIntegerField()#1-5
	comment=models.TextField(blank=True)
	datetime=models.DateTimeField()
	def __unicode__(self):
		return u'user "%s" rated on driver "%s" with grade "%s" and commented "%s" at %s' % ( self.user_traveler,self.user_driver,self.grade,self.comment,self.datetime)

class user_traveler_comments(models.Model):
#comments on travelers
	user_traveler=models.ForeignKey(user_traveler)
	user=models.ForeignKey(User)
	grade=models.PositiveSmallIntegerField()#1-5
	comment=models.TextField(blank=True)
	datetime=models.DateTimeField()
	def __unicode__(self):
		return u'user "%s" rated on a traveler "%s" with grade "%s" and commented "%s" at %s' % ( self.user,self.user_traveler,self.grade,self.comment,self.datetime)

class planfix_comments(models.Model):
#comments on planfix
	planfix=models.ForeignKey(planfix)
	user=models.ForeignKey(User)
	grade=models.PositiveSmallIntegerField()#1-5
	comment=models.TextField(blank=True)
	datetime=models.DateTimeField()
	def __unicode__(self):
		return u'user "%s" rated on a recommended travel "%s" with grade "%s" and commented "%s" at %s' % ( self.user,self.planfix.name,self.grade,self.comment,self.datetime)
