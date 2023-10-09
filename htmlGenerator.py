import json

def generate_html_from_json(json_file):
    with open(json_file, 'r') as file:
        articles = json.load(file)
    num_objects = len(articles)

    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>News Articles</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
        <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet'>
        <style>
            /* Define the 'expanded' class to initially hide content */
            
        </style>
    </head>
    <body>
        <h1 id="title">Articles {num_objects}</h1>
    '''

    for article in articles:
        html += f'''
        
            <div class="lefty">
                <h2><a href="{article['Url']}">{article['Title']}</a></h2>
                <span class="link">--{article['Source']}</span>
            </div>
            <div class="righty"
            <p class="summary">{article['Summary']}</p>
            <span class="element-title" onclick="toggleExpand(this)">Read</span>
            <p class="element-article">{article['Content']}</p></div>
        '''

    html += '''
      
        <script>
            // JavaScript to toggle the 'expanded' class on click
            function toggleExpand(element) {
                var articleElement = element.nextElementSibling;
                articleElement.classList.toggle("expanded");
            }
        </script>
    </body>
    </html>
    '''

    return html

