<?php
    // Connect to MySQL
    include("connect.php");

    // Prepare the SQL statement
      date_default_timezone_set('Asia/Jakarta');
     $dateS = date('Y-m-d H:i:s', time());
//	$jam = date('H', time());

//	if ($jam <= "4"){
//		$FT = "Malam";
//	}
//	elseif($jam <= "9"){
//		$FT = "Pagi";
//	}
//	elseif($jam <= "14"){
//		$FT = "Siang";
	//}
//	elseif($jam <= "18"){
	//	$FT = "Sore";
	//}
//	else{
//		$FT = "Malam";
//	}


    $SQL = "INSERT INTO WSN2018(date,Temperature,Humidity,CO,Note) VALUES ('$dateS','".$_GET["Temperature"]."','".$_GET["Humidity"]."','".$_GET["CO"]."','".$_GET["Note"]."')";     

    // Execute SQL statement
    mysql_query($SQL);

    // Go to the review_data.php (optional)
    header("Location: index.php");
?>