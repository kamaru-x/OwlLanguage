$(document).ready(function(){
    $('#primary').on('change',function(){
        var value = $('#primary').val();
        $('#phex').val(value);
    });

    $('#secondary').on('change',function(){
        var value = $('#secondary').val();
        $('#shex').val(value);
    });
})