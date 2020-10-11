<?php

$direction = $_POST['GO'];
$command = 'python camera.py ' . $direction;
exec($command, $output);
header("Location: access.php");