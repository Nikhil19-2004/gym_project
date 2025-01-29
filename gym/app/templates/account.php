<?php
$un=$_POST['uname'];
$ph=$_POST['phone'];
$email=$_POST['email'];
$pass=$_POST['psw'];
$rpsw=$_POST['repsw'];
$conn=mysqli_connect("localhost","root","","gym");
$query="Insert into account values('$un','$ph','$email','$pass','$rpsw')";
$result=mysqli_query($conn, $query);
if($result && $pass==$rpsw)
{
    echo"Data is inserted";
}
else{
    echo"Data is not inserted in DB";
}

?>
