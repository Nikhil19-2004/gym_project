<?php
$un=$_POST['uname'];
$pass=$_POST['psw'];
$conn=mysqli_connect("localhost","root","","ecom");
$query="Select * from account where unmae='$un'";
$data=mysqli_query($conn, $query);
while($row=mysqli_fetch_array($data))
{
    if($un==$row['uname'] && $pass==$row['psw'])
    {
        echo"you have successfully login";
    }
    else
    {
        echo"invalid user"; 
    }
    
}
?>