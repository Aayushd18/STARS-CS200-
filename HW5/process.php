<?php include 'database.php';>

<?php

// create a variable
$ID=$_POST['ID'];
$Name=$_POST['Name'];

//Execute the query

mysqli_query($connect"INSERT INTO MyUser(ID, name)VALUES('$ID','$Name')");

if(mysqli_affected_rows($connect) > 0){
	echo "<p>User Added</p>";
	echo "<a href="index.html">Go Back</a>";
} else {
	echo "User NOT Added<br />";
	echo mysqli_error ($connect);
}