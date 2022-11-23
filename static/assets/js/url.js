$(document).ready(function(){
    // $('input[name="title"]').on('keyup', function(){
    //     var value = $("input[name='title']").val();
    //     $('input[name="url"]').val(value);
    //     });

    $('input[name="title"]').on('keyup',function(){
        var value = $('input[name="title"]').val();
        var final = value.replace(/ /g,"-");
        $('input[name="url"]').val(final);
    });

    $('#title').on('keyup',function(){
        var value = $('#title').val();
        var final = value.replace(/ /g,"_");
        $('#url').val(final);
    });
})