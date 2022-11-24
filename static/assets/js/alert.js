$(document).ready(function(){
    // $('input[name="title"]').on('keyup', function(){
    //     var value = $("input[name='title']").val();
    //     $('input[name="url"]').val(value);
    //     });

    $('#op').on('blur',function(){
        var ap = $('#ap').val();
        var op = $('#op').val();
        if(op > ap){
            alert('offer price must be less than actual price')
        } 
    });
})