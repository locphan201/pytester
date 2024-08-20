# PyTester

## Introduction

This project rewrite the Python `unittest` module with better UI in the console. 

## Installation

```bash
pip install -r requirements.txt
```

## Getting started

```python
import pytester
import unittest

class TestExampleFunctions(unittest.TestCase):
    def test_function(self):
        self.assertEqual('example', 'example')

pytester.run()
```