<?php
$conn=mysqli_connect("localhost","root","","ecom");
$un=$_POST['uname'];
$email=$_POST['email'];
$sub=$_POST['subject'];
$msg=$_POST['message'];
$query="Insert into contact values('$un,'$email','$sub','$msg')";
$result=mysqli_query($conn, $query);
if($result && $email)
{
    echo"Data is inserted";
}
else{
    echo"Data is not inserted in DB";
}

?>