ArcGIS License Files/
	Licesnes for ArcGIS.  You will need to use the documentation to obtain your own.  This is empty at the moment as I am unable to share mine publically.  

GIS/
	Directory holding the GIS data you will need if you decide you want to upload data and services to the web GIS we stand up in this project.  

arcgis-webgis-ha-windows.template
	The AWS CloudFormation template JSON file for a highly available web GIS.  From: http://arcgisstore1041.s3.amazonaws.com/5686/templates/arcgis-webgis-ha-windows.template

aws_public_key.pem
	An empty file, representing that you willneed an AWS public key here for your own account.  

cf_parameters_win_HA_webgisstack.json
	The input paramaeters for our CloudFormation script.  Note that password have been blanked out.  

cloudformation_stack_creation_104.py
	Our main scirpt that runs the CLoudFormation dpeloyment.  See my documentation for more details.  

domain.pfx.txt
	An empty file representing that you will need a pfx file (SSL certificate).  Note that in the docuemtnation I mention that I use openssl to make a self-signed certificate so I do not have to purchase one.  

publish_map_services.py
	A pyhton script for publishing a web service from a map docuemnt in the GIS/ directory.  You will need ArcGIS Dekstop installed to use this.  See docuemtnation for details.  

Video Links.txt
	Links to explanation videos for this project.  


RUN THIS DEMO:
To run this demo, first seek information form the full docuemtnation in the ../documents folder.  There are certain steps that need to be taken before you proceed.  

After those have been handled (obtaining licenses, setting up a domain, putting licneses and SSL files in an S3 bucket, tweaking the cf_parameters_win_HA_webgisstack.json file) you are ready to run cloudformation_stack_creation_104.py. 

In the command line (assuming Python 2.7 and boto are isntalled) run:

C:> python cloudformation_stack_creation_104.py {AWS Access Key} {AWS Secret Key} cf_parameters_win_HA_webgisstack.json

The deployment may take up to an hour to complete.  

Once it is look to the docuemntation to see how to make an ArcGIS Server connection file and run the publish_map_services.py script (amke sure you change file paths to match the location of your GIS folder on your machine).  

C:> python publish_map_services.py

Now if you go to your CloudFOramtion stack in the AWS Console and go to the output tab then follow the link to your Protal URL and login you should be able to see your web GIS services that you published.  These can then be used in web mapping applications (see docuemtnation for more details).  