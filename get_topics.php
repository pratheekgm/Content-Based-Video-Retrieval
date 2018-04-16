<?php

error_reporting(E_ALL & ~E_NOTICE);
// $path = $_GET['path'];
// $csv_file = $_GET['csv'];

$path = $_POST['path'];
$csv_file = $_POST['csv'];

// $frames = glob($path."*.jpg");
// natsort($frames);
// $frames = array_values($frames);
// print_r($frames);
$topics = array();
$file = fopen($path.$csv_file,"r");
$i = 0;	
while(! feof($file))
  {
  	$i = $i + 1;
  	$line = fgetcsv($file);
  	if($i > 2)
  	{

  // 		$element = array(
		// 	'name' => 'Topic #'.($line[0]),
		// 	'description' => floor($line[3]),
		// 	'sources' => array(
		// 		array(
		// 			'src' => "",
		// 			'type' => ""
		// 		)
		// 	),
		// 	'thumbnail' => array(
		// 		array(
		// 			'srcset' => $path.basename($frames[$i-3]),
		// 			'type' => "image/jpeg"
		// 		),
		// 		array(
		// 			'src' => $path.basename($frames[$i-3])
		// 		)
		// 	)
		// );
  		//array_push($topics,$element);
  		array_push($topics,floor($line[3]));
  	}
  }

fclose($file);
$json = json_encode(array_slice($topics,0,-1));
echo ($json);
?>