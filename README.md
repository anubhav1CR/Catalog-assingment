# Catalog-assingment
This is the repository of assignment given by CATALOG

This project implements a simplified version of Shamir's Secret Sharing algorithm, which allows for the secure sharing of a secret among multiple parties. The code reads polynomial roots from a JSON file, decodes them from their respective bases, and calculates the constant term of the polynomial.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How to Run the Code](#how-to-run-the-code)
- [Contributing](#contributing)
- [License](#license)

## Overview

The program consists of the following main components:

1. **JSON Parsing**: Reads polynomial roots from a JSON file.
2. **Value Decoding**: Converts values from their specified bases into decimal format.
3. **Constant Term Calculation**: Calculates the constant term \( c \) of the polynomial based on the decoded roots.

## Requirements

- Python 3.x
- No external libraries are required; the code uses built-in libraries.

## Installation

1. Clone this repository to your local machine using:
   ```bash
   git clone <repository-url>
