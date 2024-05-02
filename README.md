# Playwright Future error reproducer

1. pip install -r requirements.txt
2. python main.py

### Error:

```
$ python main.py
status_code 200 | url http://httpbin.org/status/200
Future exception was never retrieved
future: <Future finished exception=TargetClosedError('Target page, context or browser has been closed')>
playwright._impl._errors.TargetClosedError: Target page, context or browser has been closed
```
