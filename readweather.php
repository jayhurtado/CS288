<html>
<head>
	<title>Weather of States</title>
</head>
<body>
<?php 
	$cnx = new mysqli('localhost', 'root', 'root', 'weather');

	if ($cnx->connect_error)
		die('Connection failed: ' . $cnx->connect_error);

	$query = 'SELECT * FROM weathertable';
	$cursor = $cnx->query($query);
	while($row = $cursor->fetch_assoc()){
		echo '<tr>';
		echo '<td>' . $row['state'] . ' ' . '</td><td>' . $row['city'] . ' ' . '</td><td>' . $row['weather'] . ' ' . '</td><td>' . $row['temperature'] . ' ' . '</td><td>' . $row['humidity'] . ' ' . '</td><td>' . $row['pressure'] . ' ' . '</td>';
		echo '</tr>';
		echo nl2br("\n");
}

	$cnx->close();
?>
</table>
</body>
</html>
