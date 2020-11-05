<?php
$date = date('Y-m-d h:i:s');
echo (">>> CLOSED $date \n");
$command = 'python close.py';
exec($command, $output);
header("Location: access.php");