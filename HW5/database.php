<?php
$connect=mysqli_connect('localhost','root','80','mydatabase');

if(mysqli_connect_errno($connect))
{
		echo 'Failed to connect';
}

?>