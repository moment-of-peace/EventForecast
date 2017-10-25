<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="resource/asset/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="resource/asset/css/bootstrap.css">
    <link rel="stylesheet" type="text/css" href="resource/asset/css/bootstrap-theme.css">
    <link rel="stylesheet" type="text/css" href="resource/css/style.css">
    <script src="resource/asset/js/jquery-3.1.1.min.js"></script>
    <script src="resource/asset/js/bootstrap.min.js"></script>
    <?php
    error_reporting(-1); // reports all errors
    ini_set("display_errors", "1"); // shows all errors
    ini_set("log_errors", 1);
    ini_set("error_log", "/tmp/php-error.log");
    date_default_timezone_set("Australia/Brisbane");
    $link = mysqli_connect('127.0.0.1', 'root','1226237');
    if(!$link){
        die('Not connected : '.mysqli_error($link));
    }
    $db = mysqli_select_db($link, 'event_forecast');
    if(!$db){
        die('Cannot use : '.mysqli_error($link));
    }
    mysqli_query( $link,"set character set 'UTF-8'");
    ?>
    <link href="https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Merriweather:300,400,400i,700,700i" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,600,700,700i,800" rel="stylesheet">
    <title>Hot News</title>
</head>
<body>
<nav class="navbar navbar-inverse">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">
                <img alt="Brand" src="resource/images/logo.png" style="height: 100%">
            </a>
        </div>
    </div>
</nav>
<!-- carousel starts -->
<div id="homeCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
        <li data-target="#myCarousel" data-slide-to="3"></li>
        <li data-target="#myCarousel" data-slide-to="4"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner" role="listbox">
        <?php
        $sql_carousel = "SELECT * FROM news WHERE news_date >= DATE_ADD(CURDATE(), INTERVAL -5 DAY) ORDER BY mention_times DESC LIMIT 0,5;";
        $result_carousel = $link->query($sql_carousel);
        $i=0;
        while($carousel=$result_carousel->fetch_assoc()){
            if($i==0){
                ?>
                <div class="item active">
                    <img src="<?=$carousel["img_url"]?>" alt="<?=$carousel["news_title"]?>" class="img-responsive">
                    <div class="carousel-caption">
                        <a href="<?=$carousel["news_url"]?>">
                            <h3><?=$carousel["news_title"]?></h3>
                        </a>
                    </div>
                </div>
            <?php    }else{?>
                <div class="item">
                    <img src="<?=$carousel["img_url"]?>" alt="<?=$carousel["news_title"]?>" class="img-responsive">
                    <div class="carousel-caption">
                        <a href="<?=$carousel["news_url"]?>">
                            <h3><?=$carousel["news_title"]?></h3>
                        </a>
                    </div>
                </div>
            <?php    }
            $i++;}
        ?>
    </div>

    <!-- Left and right controls -->
    <a class="left carousel-control" href="#homeCarousel" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#homeCarousel" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right"></span>
        <span class="sr-only">Next</span>
    </a>
</div>
<!-- carousel ends -->

<?php

?>
<div class="single-page">
    <div class="col-md-offset-2 col-md-8 content-left single-post">
        <div class="blog-posts">
            <div class="recipe-steps">
                <?php
                $pre = 0;
                $nex = 10;
                $sql_page = "SELECT * FROM news WHERE news_date >= DATE_ADD(CURDATE(), INTERVAL -5 DAY) ORDER BY mention_times DESC LIMIT $pre, $nex;";
                $result_page = $link->query($sql_page);
                if($result_page->num_rows>0){
                    $i = 1;
                    while($row = $result_page->fetch_assoc()) {?>
                        <div class="recipe-step">
                            <hr>
                            <div class="recipe-step-left">
                                <a href="<?=$row['news_url']?>" target="_blank">
                                    <img src="<?=$row["img_url"]?>" class="img-rounded">
                                </a>
                            </div>
                            <div class="recipe-step-right">
                                <div class="recipe-step-title">
                                    <a href="<?=$row["news_url"]?>" class="search-recipe-item">
                                        <p class="title" href="<?=$row["news_url"]?>"><?=$row["news_title"]?>.</p>
                                    </a>
                                </div>
                                <div class="recipe-step-text">
                                    <p><?=$row["news_description"]?></p>
                                    <div class="clearfix"></div>
                                </div>
                            </div>
                            <div class="clearfix"></div>
                        </div>
                        <?php       $i++;
                    }
                    $result_page->close();
                }
                ?>
                <div class="clearfix"></div>
                <hr>
            </div>
            <ul class="pagination search-pagination">
                <?php if (!isset($_GET["mobile"])){?>
                    <li><a href="#"><span class="glyphicon glyphicon-chevron-left"></span>&nbsp;Previous</a></li>
                    <?php
                }?>
                <?php
                $count = 10;
                for ($i=1;$i<=$count;$i++){
                    if (1 == $i){
                        ?>
                        <li class="active"><a href="#"><?=$i?></a></li>
                        <?php
                    }else{
                        ?>
                        <li><a href="#"><?=$i?></a></li>
                        <?php
                    }
                    ?>

                    <?php
                }

                ?>
                <?php if (!isset($_GET["mobile"])){?>
                    <li><a href="#">Next&nbsp;<span class="glyphicon glyphicon-chevron-right"></span></a></li>
                    <?php
                }?>
            </ul>
        </div>
        <div class="clearfix"></div>
    </div>
</div>

<script>
    $(function () {
        // change the height of carousel to make w/h = 3/1
        var cs_imgs = $('#homeCarousel .item img');
        var cs_img_width = $(cs_imgs[0]).width();
        for (i = 0; i < cs_imgs.length; i++) {
            $(cs_imgs[i]).css({'height': cs_img_width / 3 + 'px'});
            if (cs_img_width > 992) {
                $(cs_imgs[i]).parent('.item').children('.carousel-caption').css({'margin-bottom': cs_img_width / 9 + 'px'});
            } else {
                $(cs_imgs[i]).parent('.item').children('.carousel-caption').css({'margin-bottom': 0 + 'px'});
            }
        }
    });
</script>
</body>
</html>