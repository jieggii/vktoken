# vktoken
Tool for getting VK access token.
[![preview](https://asciinema.org/a/oZXWlLuODZ9K78KVNFKLdAmem.svg)](https://asciinema.org/a/oZXWlLuODZ9K78KVNFKLdAmem)

## Installation
`pip install --user vktoken`

## Usage
`vktoken [--help] [--version] [--app] [--client-id] [--client-secret] login [password]`

## Examples
* `vktoken +79652331167`  
* `vktoken --app iphone +79523311167 mypassword`
* `vktoken --client-id 3140623 --client-secret VeWdmVclDCtn6ihuP1nt +79523311167`

## Features
* You can choose builtin VK app credentials from the list: `android`, `iphone`, `ipad` and `windows-phone`.
