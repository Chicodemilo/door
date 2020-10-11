<html>

<body>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="dog.css">
        <title>
            🐶Door
        </title>
    </head>
    <p>DOG DOOR 🐶</p>
    <img src="http://192.168.1.12:8081" alt="" class="video">
    <div class="buttons">
        <form action="./run.php" method="post">
            <input type="submit" value="OPEN" name="GO">
        </form>
        <form action="./close.php" method="post">
            <input type="submit" value="CLOSE" name="GO">
        </form>
        <hr>
        <form action="./camera.php" method="post">
            <input type="submit" value="UP" name="GO">
        </form>
        <br>
        <form action="./camera.php" method="post">
            <input type="submit" value="LEFT" name="GO">
        </form>
        <form action="./camera.php" method="post">
            <input type="submit" value="RIGHT" name="GO">
        </form>
        <br>
        <form action="./camera.php" method="post">
            <input type="submit" value="DOWN" name="GO">
        </form>
    </div>

</body>

</html>