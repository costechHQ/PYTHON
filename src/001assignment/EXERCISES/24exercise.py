post = "Loving #Python and #Coding at #LkhibraAcademy"
words = post.split()
hashtags = [word for word in words if word.startswith("#")]
print(f"Hashtags: {hashtags}")
