# vktoken
A tool for getting VK access token

## Install:
`pip install vktoken`

## Run:
`vktoken [--help] [--copy] [--version] login [password] [app]`

## Examples:
* `vktoken +12025550178`  
* `vktoken --copy +12025550178  "MyPassword" iphone` 

## Features:
* Access token can be copied to the clipboard automatically if you use `--copy` key 
* You can choose any VK app from the list: `android`, `iphone`, `ipad`, `windows-phone` and `desktop`
