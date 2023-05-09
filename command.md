cmd for check memory of lib
```
pip3 list | tail -n +3 | awk '{print $1}' | xargs pip3 show | grep -E 'Location:|Name:' | cut -d ' ' -f 2 | paste -d ' ' - - | awk '{print $2 "/" tolower($1)}' | xargs du -sh 2> /dev/null | sort -hr
```