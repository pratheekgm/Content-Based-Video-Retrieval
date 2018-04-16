<?php
//extract POST variables
#error_reporting(E_ERROR | E_PARSE);
$path = $_POST['path'];
$type = $_POST['type'];

$playlist = array();
$video_dirs = array_filter(glob($path.'/*'), 'is_dir'); //get directories in an assocative array
natsort($video_dirs); //natural sort the array for accurate ordering of alphanumeric filenames
$video_dirs = array_values($video_dirs); //convert associative array into an indexed array
$arr_length = count($video_dirs);
for($i = 0 ; $i < $arr_length ; $i++){
	$fol_name = basename($video_dirs[$i]); //store folder names as simple basenames
	$element = array(
		'name' => 'Video #'.($i+1),
		'description' => $fol_name,
		'sources' => array(
			array(
				'src' => $video_dirs[$i]."/".basename($video_dirs[$i]).".".$type,
				'type' => 'video/'.$type
			)
		),
		'thumbnail' => array(
			array(
				'srcset' => $video_dirs[$i]."/thumb.jpg",
				'type' => "image/jpeg"
			),
			array(
				'src' => $video_dirs[$i]."/thumb.jpg"
			)
		)
	);
	array_push($playlist, $element);
}
echo json_encode($playlist); //print results as a json object
?>