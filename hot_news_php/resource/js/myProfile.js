var myProfile = {
    myComments: function (num,userid) {
        $.ajax({
            url: 'getMyComments.html' ,
            data: {
                userid: userid ,
                num: num
            } ,
            success: function (result) {
                var res = $.parseJSON(result);
                var pageCount = res.count;
                var list = res.list;
                $('.user-item-tbody').empty();
                for(var i=0;i<list.length;i++){
                    var comment = list[i];
                    $('.hidecontent').empty();
                    $('.hidecontent').html(comment.content);
                    var content = $('.hidecontent').text();
                    var html = '<tr>'+
                        '<td class="mycomment-title"><a target="_blank" href="passage.html?passageid='+comment.passageid+'&categoryid='+comment.categoryid+'"><p>'+comment.passageTitle+'</p></a>'+
                        '</td>'+
                        '<td class="mycomment-content"><p>'+content+'</p></td>'+
                        '<td class="mycomment-date">'+comment.date+'</td>'+
                        '<td class="mycomment-delete"><a href="#" class="my-comment-delete" data-id="'+comment.commentid+'"><span class="glyphicon glyphicon-trash"></span></a></td>'+
                        '</tr>';
                    $('.user-item-tbody').append(html);
                }
                $('.pagination').empty();
                for(var j=1;j<=pageCount;j++){
                    if(j==num)
                        $('.pagination').append('<li class="active"><a href="#" data-num="'+j+'">'+j+'</a></li>');
                    else
                        $('.pagination').append('<li><a href="#" data-num="'+j+'">'+j+'</a></li>');
                }
                myProfilePagination.initCommentClickEvent();
            }
        });
    },
    mySystemInfo: function (num,userid) {
        $.ajax({
            url: 'getSystemInfo.html' ,
            data: {
                userid: userid ,
                num: num
            } ,
            success: function (result) {
                var res = $.parseJSON(result);
                var pageCount = res.count;
                var list = res.list;
                $('.user-item-tbody').empty();
                for(var i=0;i<list.length;i++){
                    var msg = list[i];
                    var html='<tr><td class="mysysinfo-content text-left">'+msg.content+'</td><td class="mysysinfo-date">'+msg.date+'</td></tr>';
                    $('.user-item-tbody').append(html);
                }
                $('.pagination').empty();
                for(var j=1;j<=pageCount;j++){
                    if(j==num)
                        $('.pagination').append('<li class="active"><a href="#" data-num="'+j+'">'+j+'</a></li>');
                    else
                        $('.pagination').append('<li><a href="#" data-num="'+j+'">'+j+'</a></li>');
                }
                myProfilePagination.initSysinfoClickEvent();
            }
        });
    } ,
    myCollection: function (num,userid) {
        $.ajax({
            url: 'getMyCollection.html' ,
            data: {
                userid: userid ,
                num: num
            } ,
            success: function (result) {
                var res = $.parseJSON(result);
                var pageCount = res.count;
                var list = res.list;
                $('.user-item-tbody').empty();
                for(var i=0;i<list.length;i++){
                    var collection = list[i];
                    var html = '<tr>'+
                        '<td class="mycomment-title"><a target="_blank" href="passage.html?passageid='+collection.passageid+'&categoryid='+collection.categoryid+'"><p>'+collection.title+'</p></a>'+
                        '</td>'+
                        '<td class="mycomment-date">'+collection.adddate+'</td>'+
                        '<td class="mycomment-delete"><a href="#" class="my-collection-delete" data-id="'+collection.collectionid+'"><span class="glyphicon glyphicon-trash"></span></a></td>'+
                        '</tr>';
                    $('.user-item-tbody').append(html);
                }
                $('.pagination').empty();
                for(var j=1;j<=pageCount;j++){
                    if(j==num)
                        $('.pagination').append('<li class="active"><a href="#" data-num="'+j+'">'+j+'</a></li>');
                    else
                        $('.pagination').append('<li><a href="#" data-num="'+j+'">'+j+'</a></li>');
                }
                myProfilePagination.initCollectionClickEvent();
            }
        });
    } ,
    myHistory: function (num,userid) {
        $.ajax({
            url: 'getMyReadHistory.html' ,
            data: {
                userid: userid ,
                num: num
            } ,
            success: function (result) {
                var res = $.parseJSON(result);
                var pageCount = res.count;
                var list = res.list;
                $('.user-item-tbody').empty();
                for(var i=0;i<list.length;i++){
                    var history = list[i];
                    var html = '<tr>'+
                        '<td class="mycomment-title"><a target="_blank" href="passage.html?passageid='+history.passageid+'&categoryid='+history.categoryid+'"><p>'+history.title+'</p></a>'+
                        '</td>'+
                        '<td class="mycomment-date">'+history.viewdate+'</td>'+
                        '<td class="mycomment-delete"><a href="#" class="my-history-delete" data-id="'+history.historyid+'"><span class="glyphicon glyphicon-trash"></span></a></td>'+
                        '</tr>';
                    $('.user-item-tbody').append(html);
                }
                $('.pagination').empty();
                for(var j=1;j<=pageCount;j++){
                    if(j==num)
                        $('.pagination').append('<li class="active"><a href="#" data-num="'+j+'" >'+j+'</a></li>');
                    else
                        $('.pagination').append('<li><a href="#" data-num="'+j+'">'+j+'</a></li>');
                }
                myProfile.initHistoryClickEvent();
            }
        });
    }
};
var myProfilePagination = {
    initCommentClickEvent: function () {
        $('.my-comment-delete').click(function () {
            var result = confirm('确认删除这条评论吗?');
            if(result==true){
                var commentid = $(this).attr('data-id');
                $.ajax({
                    url: 'deleteComment.html' ,
                    data: {
                        commentid: commentid
                    } ,
                    success: function (result) {
                        if(result=='success')
                            myProfile.myComments(1,userid);
                    } ,
                    error: function () {
                        alert('网络连接失败，请重试');
                    }
                });
            }
        });
        $('.pagination li').click(function () {
            var num = $(this).children('a').attr('data-num');
            myProfile.myComments(num,userid);
        });
    } ,
    initCollectionClickEvent: function () {
        $('.my-collection-delete').click(function () {
            var collectionid = $(this).attr('data-id');
            $.ajax({
                url: 'deleteCollection.html' ,
                data: {
                    collectionid: collectionid
                } ,
                success: function (result) {
                    if(result=='success')
                        myProfile.myCollection(1,userid);
                } ,
                error: function () {
                    alert('网络连接失败，请重试');
                }
            });
        });
        $('.pagination li').click(function () {
            var num = $(this).children('a').attr('data-num');
            myProfile.myCollection(num,userid);
        });
    } ,
    initSysinfoClickEvent: function () {
        $('.pagination li').click(function () {
            var num = $(this).children('a').attr('data-num');
            myProfile.myComments(num,userid);
        });
    } ,
    initHistoryClickEvent: function () {
        $('.my-history-delete').click(function () {
            var historyid = $(this).attr('data-id');
            $.ajax({
                url: 'deleteReadHistory.html' ,
                data: {
                    historyid: historyid
                } ,
                success: function (result) {
                    if(result=='success')
                        myProfile.myHistory(1,userid);
                } ,
                error: function () {
                    alert('网络连接失败，请重试');
                }
            });
        });
        $('.pagination li').click(function () {
            var num = $(this).children('a').attr('data-num');
            myProfile.myHistory(num,userid);
        });
    }
};