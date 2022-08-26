# imports module
from dataclasses import dataclass
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime , date
  
today = date.today()

def maker(receiptlist,buissnessname,clientname):
	date = datetime.today().strftime('%Y-%m-%d')
	# data which we are going to display as table
	DATA = [
    		[ "Date" , "Name", "Price (GBP)" ],
	]
		
	for i in receiptlist:
		item = i["item"]
		price = i["price"]
		DATA.append([date,item,price])
		

		# creating a Base Document Template of page size A4
	pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )
	
	# standard stylesheet defined within reportlab itself
	styles = getSampleStyleSheet()
	
	# fetching the style of Top level heading (Heading1)
	title_style = styles[ "Heading1" ]
	
	# 0: left, 1: center, 2: right
	title_style.alignment = 1
	
	# creating the paragraph with 
	# the heading text and passing the styles of it
	title = Paragraph( f"{buissnessname} Date:{today}" , title_style )
	
	# creates a Table Style object and in it,
	# defines the styles row wise
	# the tuples which look like coordinates 
	# are nothing but rows and columns
	style = TableStyle(
		[
			( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
			( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
			( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
			( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
			( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
			( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
		]
	)
	
	# creates a table object and passes the style to it
	table = Table( DATA , style = style )
	
	# final step which builds the
	# actual pdf putting together all the elements
	pdf.build([ title , table ])


