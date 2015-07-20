# Datapackage CSV => JSON converter

Simple script to take as input a datapackage JSON file and convert CSV data to
JSON format, as if it were (almost) served from the CKAN datastore API.

This allows for playing around with datastore packages without having to install CKAN.

A couple of differences with the CKAN API:

* the types used in data packages don't conform to the types that are used in data packages.
* the resource ID is some kind of hash in the CKAN API, but is just the name of the dataset here.

## Usage

There are three required arguments:

* `--dir-path`: Set the base directory path for datapackage files
* `--datapackage-path`: Set the path for the datapackage.json within the base directory
* `--resource-name`: Specify the resource name within the datapackage

You can then use these commands with:

  ./parse --convert --resource-name="eiti_normalised" --dir-path="../NRGI/eiti-parser/" --datapackage-path="datapackage.json"

... which will print the output to the console. Adding ` > out.json` to the end will output to file `out.json`

## License

The MIT License (MIT)

Copyright (c) 2015 Mark Brough, Natural Resource Governance Institute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
