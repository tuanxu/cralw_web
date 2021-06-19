 <?php
$servername = "localhost";
$username = "id16977318_wp_ec276a981c7da1c7842dde3f1b061177";
$password = "=ESSzrfNwdQn&Y%5";
$dbname = "id16977318_wp_ec276a981c7da1c7842dde3f1b061177";
$tbl_users = "users";
 
$mysqli = new mysqli($servername, $username, $password, $dbname);

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$result = mysqli_query($conn, "SELECT max(ID) FROM `wp_posts`");
$row = mysqli_fetch_array($result);

    
$highest_id = $row[0];
//echo("highest_id = ".$highest_id);
 
$new_id = $highest_id + 1;

if (isset($_POST["insertsql"])) {
    
	$firstname = htmlspecialchars($_POST["firstname"]);
	$lastname = htmlspecialchars($_POST["lastname"]);
	$insertsql = $_POST["insertsql"];
	$sql = str_replace("IDREPLACEID",$new_id,$insertsql);
	//echo "firstname: $firstname lastname: $lastname insertsql: $insertsql";
	
    echo("sql = ".$insertsql);
	if ($conn->query($sql) === TRUE) {
	  echo "New record created successfully";
	} else {
	  echo "Error: " . $conn->error;
	}
	}
else
	echo "nothing";

$conn->close();
?> 