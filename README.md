# pdf-util

PDF utility.

## Prerequisite
Install the requirements prior to using the script.
```
pip install -r requirements txt
```

## Split

1. Use command to start the process.

```
python main.py split --input-file="my/input/file.pdf"
```

It will ask to put the page range. Use any page you wish to put in which can be a single or multiple page(s). For example, `1, 5-10, 11` will take page 1, 5-10, and 11 and put it in output file specified in the prompt. If output file is not specified, it will save in `output.pdf` under the same directory this script is running.