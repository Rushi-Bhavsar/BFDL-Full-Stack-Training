- Value of context should be of type dictionary type only.
```python
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    mydict = {'mylist': "Welcome to first Django Template from template/first_app directory."}
    render_obj = render(request, 'first_app/first_template.html', context=mydict)
    return render_obj
    # OR
    # return render(request, 'first_app/first_template.html', context=mydict)

```

- To dynamically insert value into html file we need to use Django Templates tags.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>First Django Template</title>
</head>
<body>
    <h1>Welcome to First Django Project.</h1>
    {{ mylist }}
</body>
</html>
```
- **Note here mylist is the key of the dictionary mydict that we pass as context to render function.
  We need to use that key inside double curly brackets only '{{  }} '.**