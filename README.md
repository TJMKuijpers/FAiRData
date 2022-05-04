<h1>Research data management</h1>
<h2> General information </h2>
This repository contains information about research data management, reproducible code, and jupyter notebooks to create metadata schemes. There are 4 main subfolders in this repository that are focused on a main topic: <br>
<ul>
  <li> Electronic Lab Notebook </li>
  <li> Reproducible code </li>
  <li> Data documentation </li>
  <li> Open Access Publishin </li>
 </ul>
 <br>
 This repository will be updated frequently with new information and guidelines.

<h2> Data package </h2>
A data package is a collection of all digital parts of a research project including data, code, texts (protocols, reports, questionnaires, meta data). The collection is created in such a way that reproducing all results is straightforward.  <br>
<br>
When creating a data package, you should keep the following three principles in mind:
<ul>
  <li>Files should be organized in a conventional folder structure</li>
  <li>Data, methods, and output should be clearly separated</li>
  <li>The computational environment should be specified</li>
</ul>

When working on your data package, you can follow the steps below:
<ul>
  <li>Think about a good folder structure</li>
  <li>Create folder structure (main directory and sub directories)</li>
  <li>Add all files needed for reproducing the results of the project</li>
  <li>Try to have the data package as clean and easy to use (add readme files to important folders)</li>
  <li>Have a peer check the data package and see if it works correctly</li>
  <li>When you finished the data package, place it in your data archive or repository</li>
</ul>

Finally, you can use the following checklist to see if you included all relevant files:
- [ ] Readme file(s)
- [ ] Metadata file
- [ ] Documentation file 
- [ ] Raw data
- [ ] Processed data
- [ ] Protocols 
- [ ] Methodologies 
- [ ] Scripts 


<h2> Data documentation</h2>
<h3> Metadata schemes </h2>
This is the testing environment to develop a workflow to build and test a FAIR metadata documentation based on the FAIR principles. We include different metadata schemes including the DataCite schema. Furthermore, it is possible to check your documentation against a predifed set of key words for a specific research area. </br>

<h4> DataCite </h4>
The DataCite schema provides persistent identifiers (DOIs) for research data and other research outputs. <br>
For more information visit the <a href="https://datacite.org">DataCite website </a>

<h4> Software requirements </h4>
<ol>
  <li>Python (version 3.8.5)</li>
  <li>Pandas (version 1.1.3)</li>
  <li>chardet (version 3.0.4)</li>
</ol>

<h4> Test the FAIRness of your data </h4>
To start and test the FAIRness of your data, load the document you want to test: <br> 
 
```python
working_document='DataCiteExample.txt'
data_to_check=pd.read_csv('DataCiteExample.txt',sep='\t')
data_to_json=create_json_object(data_to_check)
```
 
After you succesfully loaded your document, the first test will try and identify if you use a FAIR file format: <br>
```python
fairness_file=CheckFairification(file_name='DataCiteExample.txt')
fairness_file.score_fairness_data_type()
```

The second test can be used to identify if your document contains the required fields based on an xml schema. <br>
Here, we will test if our document meets the DataCite standards: <br>
 
 ```python
 check_data=CheckDataValidity(Data=data_json,type='DataCite')
check_data.set_the_mandatory_fields()
check_data.check_required_fields()
print('Test 1: check if all required fields are present: %s' % check_data.required_fields)
check_data.check_for_na()
print('Test 2: json object contains no NA values: %s ' % check_data.na_checked)
check_data.check_format_of_date()
print('Test 3: format date check: %s' % check_data.correct_format)
print('Overall the metadata %s the test. Please revise your documentation.' % check_data.required_fields)
 ```
 
The test output can be used to improve your documentation before you upload your dataset to a repository or archive. 

 

<h3> software license </h3>
<i>Copyright (c) 2022, TJM Kuijpers <br>
All rights reserved. <br>

This source code is licensed under the BSD-3-Clause. <br></i>
