$src = $args[0]; 
(Get-ChildItem $src -Recurse).FullName | % { Process {
    Start-Process Python -NoNewWindow -ArgumentList "./convert.py $($_)" } };