import re

def find_syntax_error(code):
    try:
        compile(code, filename='<string>', mode='exec')
        print("No syntax errors found.")
    except SyntaxError as e:
        return e.lineno
    return None

def Filter(txt):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, txt, re.DOTALL)

    if matches:
        python_code = matches[0].strip()
        return python_code
    else:
        return None
    