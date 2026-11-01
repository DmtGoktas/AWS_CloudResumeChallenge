Demet Goktas portfolio update

Files:
- index1.html: Home page (keeps the existing S3 website index filename)
- resume.html: Resume page
- cloud-resume-challenge.html: Technical article
- style2.css: Shared responsive styling
- script.js: Visitor counter (endpoint preserved from the uploaded source)

Deployment:
Upload these files to the root of the existing S3 website bucket, replacing the
matching old files. Keep the existing CloudFront distribution and frontend
GitHub Actions workflow.

Important:
The visitor counter API URL in script.js has been preserved exactly from the
uploaded crc.txt source. If that URL is not the currently working endpoint,
replace it with the active API URL before deployment.
