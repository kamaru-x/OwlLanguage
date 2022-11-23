$(document).ready(function(){

    $('div[name="div1"]').hide();
    $('input[name="check1"]').on('click', function(){
    if ( $(this).prop('checked') ) {
        $('div[name="div1"]').show();
    } 
    else {
        $('div[name="div1"]').hide();
    }
    });

    $('div[name="div2"]').hide();
    $('input[name="check2"]').on('click', function(){
    if ( $(this).prop('checked') ) {
        $('div[name="div2"]').show();
    } 
    else {
        $('div[name="div2"]').hide();
    }
    });

})