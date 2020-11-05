<?php
$date = date('Y-m-d h:i:s');
echo (">>> OPEN $date \n");
$command = 'python motor.py';
exec($command, $output);
header("Location: access.php");