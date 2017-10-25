/**
 * Created by Charles on 30/05/2017.
 */
$(function(){
    $('a#changePhoto').click(function () {
        $('#img-upload').trigger('click');
    });
    $('#img-upload').change(function () {
        var data = new FormData($('#img-upload-form')[0]);
        $.ajax({
            url: '../services/uploadFile.php',
            cache: false,
            contentType: false,
            processData: false,
            type: 'POST',
            data: data,
            success: function (data) {
                var r = $.parseJSON(data);
                if(r.status == 1){
                    $('.user-avatar-lg').attr("src",r.result);
                }else{
                    alert(r.result);
                }
                console.log(r);
            }
        });
    });
});

