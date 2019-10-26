# mail-sender.py  
ARinteg: api which allows you to send pdf to mail  
it contain function email() that takes:  
 1. list of strings;
 2. email from which you want to send an email containing attachments in the form of pdf files with elements of the input list;
 3. password of this email  
 4. email to send message  
function also saves this pdf files in root catalog.  
to delete this files use function delete() that takes same list of strings.  
Function email() use fpgf package. to install it write in command line:  
 python -m pip install fpdf
