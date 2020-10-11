<?php

// echo ("CLOSED");
$command = 'python camera.py Taco!!';
exec($command, $output);
header("Location: access.php");