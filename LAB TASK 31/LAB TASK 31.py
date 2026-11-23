
import webbrowser

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>My AI Blog</title>
</head>
<body>

    <h1>My Artificial Intelligence Blog</h1>

    <h2>Introduction to AI</h2>

    <p>
        Artificial Intelligence enables machines to learn
        and perform tasks intelligently.
    </p>

    <a href="https://www.wikipedia.org" target="_blank">
        Click here to learn more
    </a>

    <h2>Machine Learning</h2>

    <p>Machine Learning is a branch of Artificial Intelligence.</p>

    <img src="https://via.placeholder.com/300"
         alt="AI Image">

</body>
</html>
"""

with open("ai_blog.html", "w", encoding="utf-8") as file:
    file.write(html_code)

webbrowser.open("ai_blog.html")

print("AI Blog opened successfully!")
