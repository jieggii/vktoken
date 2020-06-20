# vktoken
A tool for getting VK access token

## Installation
`pip install vktoken`

## Usage
`vktoken [--help] [--copy] [--version] [--quiet] login [password] [app]`

## Examples
* `vktoken +12025550178`  
* `vktoken --copy +12025550178  "MyPassword" iphone` 
* `vktoken --quiet --copy +12025550178`

## Features
* Access token can be copied to the clipboard automatically if you use `--copy` key 
* You can choose any VK app from the list: `android`, `iphone`, `ipad`, `windows-phone` and `desktop`
