<?php
extract($_GET);
chdir("Demo");
$command = escapeshellcmd('python cosine.py '.$query.' > output_final.txt' );
$output=array();
exec($command,$output);
foreach($output as $line) {
    echo $line;
};

?>