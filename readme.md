# AWS CloudFormation – Deploying Web GIS Technology

## Video Links
•	[Short](https://www.youtube.com/watch?v=jNO5wFPRBO0&feature=youtu.be) 2 min.
•	[Long](https://www.youtube.com/watch?v=zd74Km1zFqA&feature=youtu.be) 15 min.
•	[Live Demo](https://www.youtube.com/watch?v=PpL-0VdDCPs) 15 min.

## Documentation
•	[One Pager](https://drive.google.com/file/d/0B51pDDuVyPVTX0h5R2xlYVp2dmM/view?usp=sharing)
•	[Full Documentation](https://drive.google.com/file/d/0B51pDDuVyPVTQ1NoSGZGX1FqdzA/view?usp=sharing)

## Problem/Scenario
Configure and deploy a web geographic information systems (GIS) solution to Amazon Web Services (AWS) using the AWS Python SDK and AWS CloudFormation.  The web GIS system will consist of an Esri ArcGIS Server, data store, web adapter, web server, and Portal for ArcGIS (web based admin software).  Upon deployment, geospatial data will be loaded onto the web GIS and configured to output web mapping services for use in web mapping applications.  

## Description
AWS CloudFormation serves as a platform for infrastructure as code.  It allows you to quickly spin up many cloud resources and configure software on those resources through command line and SDKs.  

## Benefits
Deploying a web GIS in the cloud is significantly cheaper than hosting all of the hardware and software required to do so locally or in a data center.  Furthermore, it provides high availability and elasticity that would otherwise require non-trivial computing resources and a large time and money investment.  Using AWS CloudFormation to launch a web GIS (it can also be done manually or with GUI software) gives a nice balance of ease of use and configuration control while providing templates with best management practices to get started quickly.  

Data Sets:
Public GIS data from the City of Richmond, VA will be used to populate the web GIS’s data store (which will handle the data conversion and management process) with sample datasets to be used in web mapping applications.  Data will include:
•	Municipal boundaries (add URL and file/name size)
•	Road centerlines
•	Trails
•	Hydrology
•	Vegetation

## Operating System:
I am using Windows 10 and deploying to Windows servers, though AMIs for Ubuntu exist as well.  Examples will be for Windows servers.  

## Software
•	Esri Developer Network (EDN) License (can be obtained from Harvard Center for Geographic Analysis)
•	Esri ArcGIS for Desktop
•	Python version 2.7
•	AWS Python SDK - Boto

## Overview of Steps
•	Obtain licenses
•	Created or purchase SSL certificate (must also have a web domain)
•	Create S3 bucket and upload licenses and SSL certificate
•	Alter parameters in JSON file
•	Run Python script and monitor for when stack finishes
•	Run scripts to publish web GIS services
•	Consume web GIS services in a web mapping application

## Summary:
This application is used to store and serve out GIS data for use in highly available web GIS applications.  It will require a bit of understanding of GIS and does have a fair bit of overhead work required to obtain licenses for GIS software.  The stack takes about an hour to deploy and the AWS resources used are a bit on the pricey side.  If you work in the GIS field or are interested in it, you may find interest in this application as it is significantly easier to deploy compared to traditional methods of deploying a web GIS.
