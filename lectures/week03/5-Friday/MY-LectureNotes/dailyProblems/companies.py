import data 

#? Loop through the companies data and display logo image and company name on an html page. 
#* to run the file:  python3 companies.py > index.html

companies = data.data

print(companies)

html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>  
    
        body{
            margin:0px;
        }

        div{
            display: flex;
            height: 50px;
        }

        img{
            width: 100px;
        }
    </style>
</head>
<body>
"""

for i in companies:
    html += f'\t <div>\n\t\t<h2>{i["business_name"]}</h2>\n\t\t<img src="{i["logo"]}"></div>\n'

html += """

</body>
</html>

"""

print(html)