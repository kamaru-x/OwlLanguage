$(document).ready(function(){
    // $('input[name="title"]').on('keyup', function(){
    //     var value = $("input[name='title']").val();
    //     $('input[name="url"]').val(value);
    //     });

    $('input[name="title"]').on('keyup',function(){
        var value = $('input[name="title"]').val();
        var final = value.replace(/ /g,"_");
        var url = ('https://www.testsite/'+final+'.com')
        $('input[name="url"]').val(url);
    });
})