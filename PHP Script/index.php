<?php 
    // Start MySQL Connection
    include('connect.php'); 

      date_default_timezone_set('Asia/Jakarta');
     $dateS = date('Y-m-d H:i:s', time());
    echo "Server Time : " . $dateS;


?>

<html>
<head>
    <title>WSN 2018</title>

    <style type="text/css">
        .table_titles, .table_cells_odd, .table_cells_even {
                padding-right: 20px;
                padding-left: 20px;
                color: #000;
        }
        .table_titles {
            color: #FFF;
            background-color: #666;
        }
        .table_cells_odd {
            background-color: #CCC;
        }
        .table_cells_even {
            background-color: #FAFAFA;
        }
        table {
            border: 2px solid #333;
        }
        body { font-family: "Trebuchet MS", Arial; }
    </style>
</head>

    <body>
	<h1>
        	<center>
			<font size="5" color="black">Air Quality Monitoring System (AQMS)</font>
		</center>
	</h1>

	<h1>
		<center>


    <table border="0" cellspacing="0" cellpadding="4">
      <tr>
            <td class="table_titles">No.</td>
            <td class="table_titles">Date and Time</td>
            <td class="table_titles">Temperature</td>
            <td class="table_titles">Humidity</td>
		 <td class="table_titles">CO</td>
	 <td class="table_titles">Note</td>
          </tr>

<?php


    // Retrieve all records and display them
    $feeder = mysql_query("SELECT * FROM WSN2018");
    // Used for row color toggle
    $oddrow = true;


    // process every record WQMC
    while( $row = mysql_fetch_array($feeder))
    {
        if ($oddrow) 
        { 
            $css_class=' class="table_cells_odd"';

        }
        else
        { 
            $css_class=' class="table_cells_even"'; 

        }

        $oddrow = !$oddrow;



        echo '<tr>';
        echo '   <td'.$css_class.'>'.$row["id"].'</td>';
        echo '   <td'.$css_class.'>'.$row["date"].'</td>';
        echo '   <td'.$css_class.'>'.$row["Temperature"].'</td>';
        echo '   <td'.$css_class.'>'.$row["Humidity"].'</td>';
	  echo '   <td'.$css_class.'>'.$row["CO"].'</td>';
	echo '   <td'.$css_class.'>'.$row["Note"].'</td>';
        echo '</tr>';
    }

?>
    </table>

		</center>
	</h1>

   	<h1>
		<center>
			<font size="3" color="black">|| Oskar Natan - 1020171004 || WSN 2018 ||</font>
		</center>

		<center>
			<font size="5" color="blue">POLITEKNIK </font>				<font size="5" color="yellow">ELEKTRONIKA 					</font>				
			<font size="5" color="blue">NEGERI 						SURABAYA</font>
		</center>

	</h1>

    </body>
</html>