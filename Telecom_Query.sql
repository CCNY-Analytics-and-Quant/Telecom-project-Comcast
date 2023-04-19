--Data Extraction
SELECT * 
FROM dbo.telecom_zipcode_population tzp
INNER JOIN dbo.telecom_customer_churn tcc
ON tzp.zip_code = tcc.Zip_code
